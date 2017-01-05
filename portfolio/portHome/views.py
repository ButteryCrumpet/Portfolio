from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    frontend_projects = Project.objects.filter(type='Frontend')
    backend_projects = Project.objects.filter(type='Backend')
    return render(request, 'portHome/home.html', {'frontend_projects': frontend_projects, 'backend_projects': backend_projects})
