from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import UploadFileForm

# Create your views here.

def index(request):
    """
    A view to return the index page
    """
    return render(request, 'home/index.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_name = file.name

            # Save the file to the default storage (which is S3 if configured)
            file_path = default_storage.save(file_name, ContentFile(file.read()))

            return render(request, 'home/upload_sucess.html', {'file_url': default_storage.url(file_path)})
    else:
        form = UploadFileForm()
    return render(request, 'home/upload.html', {'form': form})