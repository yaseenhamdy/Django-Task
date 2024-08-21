from rest_framework import serializers
from .models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField()  #

    class Meta:
        model = Employee
        fields = ['id','name', 'age', 'department_name']

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
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
