from django.urls import path, include
from .views import handle_large_file_upload

urlpatterns = [
    path('handle_large_file_upload/', handle_large_file_upload, name='handle_large_file_upload')
]
