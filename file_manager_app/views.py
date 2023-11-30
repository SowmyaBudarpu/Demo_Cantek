# file_manager_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UploadedFile
from .forms import FileUploadForm

def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'file_manager_app/file_list.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'file_manager_app/upload_file.html', {'form': form})

def download_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response
