Employee and Department Management System

Overview

This Django project provides a web-based system for managing employees and departments. It includes CRUD (Create, Read, Update, Delete) operations for both Employee and Department models using Django REST Framework.

Features

- Department Management:
  - List all departments
  - Create a new department
  - Retrieve details of a specific department
  - Update department details
  - Delete a department

- Employee Management:
  - List all employees with calculated age
  - Create a new employee (by providing name, date of birth, and department)
  - Retrieve details of a specific employee
  - Update employee details
  - Delete an employee

Installation

To get started with this project, follow these steps:

1. Clone the repository:
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   - On Windows:
     venv\Scripts\activate
   - On macOS/Linux:
     source venv/bin/activate

4. Install dependencies:
   Install the required packages using the requirements.txt file:
   pip install -r requirements.txt

5. Apply migrations:
   python manage.py migrate

6. Create a superuser (optional, for accessing the Django admin interface):
   python manage.py createsuperuser

7. Run the development server:
   python manage.py runserver
   The application will be accessible at http://127.0.0.1:8000/.

API Endpoints

Department Endpoints

- GET /api/departments/: List all departments
- POST /api/departments/: Create a new department
- GET /api/departments/{id}/: Retrieve a specific department by ID
- PUT /api/departments/{id}/: Update a specific department by ID
- DELETE /api/departments/{id}/: Delete a specific department by ID

Employee Endpoints

- GET /api/employees/: List all employees with calculated age
- POST /api/employees/: Create a new employee
- GET /api/employees/{id}/: Retrieve a specific employee by ID
- PUT /api/employees/{id}/: Update a specific employee by ID
- DELETE /api/employees/{id}/: Delete a specific employee by ID

Running Tests

To run tests for this project, use the following command:
python manage.py test

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements

- Django (https://www.djangoproject.com/)
- Django REST Framework (https://www.django-rest-framework.org/)

Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

Contact

For any questions or feedback, please contact [your email address].
