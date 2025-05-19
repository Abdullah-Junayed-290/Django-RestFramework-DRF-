from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer

# Create your views here.
@api_view(["GET"])
def student_list(request):
    students = Student.objects.all()
    serializers = StudentSerializer(students, many=True)
    return Response(serializers.data)

@api_view(["GET"])
def teacher_list(request):
    teachers = Teacher.objects.all()
    serializers = TeacherSerializer(teachers, many=True)
    return Response(serializers.data)
@api_view(["POST"])    
def student_create(request):
  serializer = StudentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors)

@api_view(["POST"])
def teacher_create(request):
  serializer = TeacherSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors)