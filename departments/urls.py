from django.urls import path
from . import views

urlpatterns = [
    path('add-department/', views.add_department, name='add_department'),
    path('departments/', views.get_departments, name='get_departments'),
    path('delete-department/<int:pk>/', views.delete_department, name='delete_department'),
    path('update-department/<int:pk>/', views.update_department, name='update_department'),

]