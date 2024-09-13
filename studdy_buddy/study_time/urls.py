from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_study_time/', views.add_study_time, name='add_study_time'),
    path('delete_study_time/<int:pk>/', views.delete_study_time, name='delete_study_time'),
    path('add_material/', views.add_material, name='add_material'),
    path('delete_material/<int:pk>/', views.delete_material, name='delete_material'),
]
