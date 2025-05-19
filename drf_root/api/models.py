from django.db import models

# Create your models here.

class Student(models.Model):
    City_Name = [
    ("SM", "Samogram"), 
    ("SG", "Salimganj"), 
    ("BK", "Borikandi"),
    ("BD", "Badda"),
    ("KS", "Kolasing")
    ]
    
    
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    city = models.CharField(max_length=100, choices=City_Name)
    
    def __str__(self):
        return self.name
        
class Teacher(models.Model):
    Subjects = [
    ("BN", "Bangla"),
    ("EN", "English"),
    ("ICT", "Information and Communication Technology"),
    ]
    
    City_Name = [
    ("SM", "Samogram"), 
    ("SG", "Salimganj"), 
    ("BK", "Borikandi"),
    ("BD", "Badda"),
    ("KS", "Kolasing")
    ]
    
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=100, choices=Subjects)
    city = models.CharField(max_length=100, choices=City_Name)
    
    def __str__(self):
        return self.name