from django.db import models

from departments.models import Department

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    
    def __str__(self):
        return self.name 