
from rest_framework import serializers
from .models import Employee, Department
from datetime import date

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField()
    age = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'day', 'month', 'year', 'age', 'department_name']

    def validate_department_name(self, value):
        try:
            department = Department.objects.get(name=value)
        except Department.DoesNotExist:
            raise serializers.ValidationError("Department does not exist.")
        except Department.MultipleObjectsReturned:
            raise serializers.ValidationError("Multiple departments found with the same name.")
        return department

   
    def get_age(self, obj):
        today = date.today()
        birthdate = date(obj.year, obj.month, obj.day)
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age




