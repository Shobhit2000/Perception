from django.urls import path, include
from .views import create_dashboard, find_all_dashboards

urlpatterns = [
    path('create_dashboard/', create_dashboard, name='create_dashboard'),
    path('find_all_dashboards/', find_all_dashboards, name='find_all_dashboards')
]
