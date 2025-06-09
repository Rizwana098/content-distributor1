from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import SharedFile  

# @login_required
def home_view(request):
    # shared_files = SharedFile.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'index.html' )#,{'shared_files': shared_files})
