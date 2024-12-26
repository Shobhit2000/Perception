from django.urls import path, include
from .views import create_dashboard, find_all_dashboards, find_dashboard, delete_dashboard, delete_all_dashboards, update_dashboard

urlpatterns = [
    path('create_dashboard/', create_dashboard, name='create_dashboard'),
    path('delete_all_dashboards/', delete_all_dashboards, name='delete_all_dashboards'),
    path('delete_dashboard/', delete_dashboard, name='delete_dashboard'),
    path('find_all_dashboards/', find_all_dashboards, name='find_all_dashboards'),
    path('find_dashboard/', find_dashboard, name='find_dashboard'),
    path('update_dashboard/', update_dashboard, name='update_dashboard')
]
