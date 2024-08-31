
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

    def create(self, validated_data):
        department = validated_data.pop('department_name')
        return Employee.objects.create(department_name=department, **validated_data)
    
    def update(self, instance, validated_data):
        department = validated_data.pop('department_name', None)
        if department:
            instance.department_name = department

        instance.name = validated_data.get('name', instance.name)
        instance.day = validated_data.get('day', instance.day)
        instance.month = validated_data.get('month', instance.month)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance

    def get_age(self, obj):
        today = date.today()
        birthdate = date(obj.year, obj.month, obj.day)
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

