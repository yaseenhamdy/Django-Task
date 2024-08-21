from django.urls import path
from . import views

urlpatterns = [
    path('add-employee/', views.add_employee, name='add_employee'),  
    path('get-employees/', views.get_employees, name='get_employees'),
    path('delete-employee/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('update-employee/<int:pk>/', views.update_employee, name='update_employee'),

   
]
