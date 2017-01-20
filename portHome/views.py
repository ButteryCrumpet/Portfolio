from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    frontend_projects = Project.objects.filter(type='Frontend')
    backend_projects = Project.objects.filter(type='Backend')
<<<<<<< HEAD
    return render(request, 'porthome/home.html', {'frontend_projects': frontend_projects, 'backend_projects': backend_projects})
=======
    return render(request, 'portHome/home.html', {'frontend_projects': frontend_projects, 'backend_projects': backend_projects})

def about_me(request):
    return render(request, 'portHome/about_me.html')
>>>>>>> f3de1362ef943f5d959e5a412aaecbf4f4e03314
