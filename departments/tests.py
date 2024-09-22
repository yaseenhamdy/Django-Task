from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Department

class DepartmentAPITestCase(APITestCase):
    def setUp(self):
        # Create a department for testing
        self.department = Department.objects.create(name='HR', code=101)
        self.valid_payload = {
            'name': 'Finance',
            'code': 102
        }
        self.invalid_payload = {
            'name': '',  # Invalid because name cannot be empty
            'code': 102
        }
        self.url = reverse('department-list')  # Adjust based on your URL configuration

    def test_create_department_success(self):
        response = self.client.post(self.url, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Department created successfully")

    def test_create_department_failure(self):
        response = self.client.post(self.url, self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)  # Check for validation error on name

    def test_get_department_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure the list contains the existing department

    def test_update_department_success(self):
        url = reverse('department-detail', args=[self.department.id])  # Adjust based on your URL configuration
        response = self.client.put(url, {'name': 'Updated HR', 'code': 103})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated HR')

    def test_update_department_failure(self):
        url = reverse('department-detail', args=[self.department.id])  # Adjust based on your URL configuration
        response = self.client.put(url, {'name': '', 'code': 103})  # Invalid because name cannot be empty
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)  # Check for validation error on name

    def test_delete_department_success(self):
        url = reverse('department-detail', args=[self.department.id])  # Adjust based on your URL configuration
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Department.objects.filter(id=self.department.id).exists())  # Ensure it's deleted

    def test_delete_department_not_found(self):
        url = reverse('department-detail', args=[9999])  # Non-existent ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_department_detail_success(self):
        url = reverse('department-detail', args=[self.department.id])  # Adjust based on your URL configuration
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.department.name)

    def test_get_department_detail_not_found(self):
        url = reverse('department-detail', args=[9999])  # Non-existent ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
