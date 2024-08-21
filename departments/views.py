from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Department
from .serializers import DepartmentSerializer

@api_view(['POST'])
def add_department(request):
    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Added successfully", "status": status.HTTP_201_CREATED}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_departments(request):
    departments = Department.objects.all() 
    serializer = DepartmentSerializer(departments, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK) 


@api_view(['DELETE'])
def delete_department(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({"error": "Department not found."}, status=status.HTTP_404_NOT_FOUND)

    department.delete()
    return Response({"message": "Department deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_department(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({"error": "Department not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = DepartmentSerializer(department, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    