# from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee
from departments.models import Department

class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        # Create a department for the employee

        self.department = Department.objects.create(name='Engineering')

        # Create an employee instance for testing

        self.employee = Employee.objects.create(
            name='John Doe',
            day=15,
            month=6,
            year=1990,
            department_name=self.department
        )

    def test_create_employee(self):

        """Happy scenario: Create a new employee."""

        url = reverse('employee-list')  # Adjust if your URL pattern is different
        data = {
            'name': 'Jane Smith',
            'day': 20,
            'month': 8,
            'year': 1992,
            'department_name': self.department.name
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)
        self.assertEqual(Employee.objects.get(id=2).name, 'Jane Smith')

    def test_create_employee_missing_fields(self):
        """Bad scenario: Create an employee with missing fields."""
        url = reverse('employee-list')  # Adjust if your URL pattern is different
        data = {
            'day': 20,
            'month': 8,
            'year': 1992,

            # Missing name and department_name
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertIn('department_name', response.data)

    def test_get_all_employees(self):
        """Happy scenario: Get all employees."""
        url = reverse('employee-list')  # Adjust if your URL pattern is different
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Initially, only 1 employee should exist

    def test_update_employee(self):
        """Happy scenario: Update an existing employee."""
        url = reverse('employee-detail', kwargs={'pk': self.employee.pk})  # Adjust if your URL pattern is different
        data = {
            'name': 'John Updated',
            'day': 15,
            'month': 6,
            'year': 1991,
            'department_name': self.department.name
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.name, 'John Updated')

    def test_update_employee_invalid_department(self):
        """Bad scenario: Update employee with a non-existent department."""
        url = reverse('employee-detail', kwargs={'pk': self.employee.pk})  # Adjust if your URL pattern is different
        data = {
            'name': 'John Updated',
            'day': 15,
            'month': 6,
            'year': 1991,
            'department_name': 'Nonexistent Department'  # Invalid department
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_employee(self):

        """Happy scenario: Delete an employee."""
        
        url = reverse('employee-detail', kwargs={'pk': self.employee.pk})  # Adjust if your URL pattern is different
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)  # Employee should be deleted

    def test_delete_nonexistent_employee(self):
        """Bad scenario: Attempt to delete an employee that doesn't exist."""
        url = reverse('employee-detail', kwargs={'pk': 999})  # Invalid ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_employee_invalid_department(self):

        """Bad scenario: Create an employee with a non-existent department."""

        url = reverse('employee-list')  # Adjust if your URL pattern is different
        data = {
            'name': 'Invalid Employee',
            'day': 20,
            'month': 8,
            'year': 1992,
            'department_name': 'Nonexistent Department'  # Invalid department
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_employee_details(self):
        """Happy scenario: Get details of a specific employee."""
        url = reverse('employee-detail', kwargs={'pk': self.employee.pk})  # Adjust if your URL pattern is different
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.employee.name)

    def test_get_nonexistent_employee(self):
        """Bad scenario: Attempt to get details of a non-existent employee."""
        url = reverse('employee-detail', kwargs={'pk': 999})  # Invalid ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_employee_invalid_date(self):
        """Bad scenario: Create an employee with invalid date values."""
        url = reverse('employee-list')  # Adjust if your URL pattern is different
        data = {
            'name': 'Invalid Date Employee',
            'day': 32,  # Invalid day
            'month': 13,  # Invalid month
            'year': 1992,
            'department_name': self.department.name
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

