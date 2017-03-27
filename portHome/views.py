from django.shortcuts import render
from .models import Project, AdditionalImage

# Create your views here.
def home(request):
    frontend_projects = Project.objects.filter(type='Frontend')
    backend_projects = Project.objects.filter(type='Backend')
    return render(request, 'portHome/home.html', {'frontend_projects': frontend_projects, 'backend_projects': backend_projects})

def about_me(request):
    return render(request, 'portHome/about_me.html')

def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    try:
        additionalImages = AdditionalImage.objects.get(project = project)
    except AdditionalImage.DoesNotExist:
        additionalImages = []
    return render(request, 'portHome/details.html', {'project': project, 'images': additionalImages})
