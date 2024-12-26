from django.urls import path, include
from .views import create_dashboard, find_all_dashboards, find_dashboard

urlpatterns = [
    path('create_dashboard/', create_dashboard, name='create_dashboard'),
    path('find_all_dashboards/', find_all_dashboards, name='find_all_dashboards'),
    path('find_dashboard/', find_dashboard, name='find_dashboard')
]
