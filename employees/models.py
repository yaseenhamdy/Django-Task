from django.db import models
from departments.models import Department

class Employee(models.Model):
    name = models.CharField(max_length=50)
    day = models.PositiveIntegerField(default=1)
    month = models.PositiveIntegerField(default=1)
    year = models.PositiveIntegerField(default=2000)
    department_name = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='employees', null=True)

    def __str__(self):
        return self.name
