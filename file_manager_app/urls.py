
# file_manager_app/urls.py

from django.urls import path
from .views import file_list, upload_file, download_file

urlpatterns = [
    path('', file_list, name='file_list'),
    path('upload/', upload_file, name='upload_file'),
    path('download/<int:file_id>/', download_file, name='download_file'),
]
