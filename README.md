# Django Full Authentication System

This is a complete Django-based authentication system built by **Muthoni Gathiithi**. It includes user registration, login, logout, and error handling features. The system is ideal for learning and implementing real-world Django authentication workflows with best practices.

## 🚀 Features

- User registration with form validation
- Login and logout functionality
- Secure password handling
- Custom error handling for better user experience
- Modular structure with templates, views, and models
- Django form handling and redirections

## 🛠️ Technologies Used

- Python
- Django (latest stable version)
- SQLite (default development database)
- HTML (with Django templates)

## 🗂️ Project Structure

django_Full_Authentication_System/
│
├── Authentication/ # Main Django project folder
│ ├── settings.py # Project settings
│ ├── urls.py # Root URL configuration
│ ├── wsgi.py, asgi.py # Server interfaces
│
├── accounts/ # Core app for authentication
│ ├── templates/accounts/ # HTML templates
│ ├── views.py # View logic (login, register, logout)
│ ├── models.py # Custom user model (if any)
│ ├── forms.py # User input forms
│ ├── urls.py # App-specific URLs
│ ├── admin.py, apps.py # Admin and config
│ └── migrations/ # Database migration files
│
├── db.sqlite3 # Default database
└── manage.py # Django management script

bash
Copy
Edit

## 🧪 How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MuthoniGathiithi/django_Full_Authentication_System.git
   cd django_Full_Authentication_System
Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2.**Install dependencies**:

pip install -r requirements.txt

3.**Run migrations**:

python manage.py migrate

4.**Start the development server**:

python manage.py runserver
Visit http://127.0.0.1:8000/accounts/register/ to register a new user.
