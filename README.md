# Django REST Framework (DRF) Learning Project

This repository is a learning-based project created to explore and understand Django REST Framework (DRF). It demonstrates how to build RESTful APIs using Django, with hands-on examples of serializers, views, and model integrations.

## Features

- Simple API development using DRF
- Basic CRUD operations
- DRF serializers and viewsets
- URL routing for APIs
- Educational and beginner-friendly structure

## Technologies Used

- Python 3.8+
- Django
- Django REST Framework

## Getting Started

Follow these steps to run this project locally:

### Prerequisites

- Python installed on your system
- `pip` package manager
- (Optional) Virtual environment tool

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Abdullah-Junayed-290/Django-RestFramework-DRF-.git
   cd Django-RestFramework-DRF-
   ```

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**

   Visit `http://127.0.0.1:8000/` in your browser to explore the APIs.

## Project Structure

```
Django-RestFramework-DRF-/
â”œâ”€â”€ drf_root/
â”‚   â”œâ”€â”€ admin.py
â”‚   â”œâ”€â”€ apps.py
â”‚   â”œâ”€â”€ models.py
â”‚   â”œâ”€â”€ serializers.py
â”‚   â”œâ”€â”€ views.py
â”‚   â”œâ”€â”€ urls.py
â”œâ”€â”€ manage.py
â”œâ”€â”€ requirements.txt
â””â”€â”€ README.md
```

## Contribution

Pull requests are welcome. If you'd like to improve or extend this project, feel free to fork the repository and submit a PR.

## License

This project is licensed under the MIT License.
