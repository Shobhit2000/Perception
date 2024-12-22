from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .serializer import UploadSerializer
from django.http import HttpResponse


@api_view(['POST'])
def handle_large_file_upload(request):
    uploaded_file = request.FILES['file']
    filename = uploaded_file.name

    file_path = 'files/test_files/' + filename

    if uploaded_file.multiple_chunks():
        chunk_size = 10 * 1024 * 1024  # 10MB chunk size
        with open(file_path, 'wb') as f:
            for chunk in uploaded_file.chunks(chunk_size=chunk_size):
                f.write(chunk)
    else:
        file_data = uploaded_file.read()
        with open(file_path, 'wb') as f:
            f.write(file_data)

    return HttpResponse('File uploaded successfully!')