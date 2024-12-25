from django.urls import path, include
from .views import create_dashboard

urlpatterns = [
    path('create_dashboard/', create_dashboard, name='create_dashboard')
]
