from django.shortcuts import render
from .models import Project, AdditionalImage

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portHome/home.html', {'projects': projects, 'page': 'home'})

def about_me(request):
    return render(request, 'portHome/about_me.html', {'page': 'about_me'})

def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    try:
        additionalImages = AdditionalImage.objects.get(project = project)
    except AdditionalImage.DoesNotExist:
        additionalImages = []
    return render(request, 'portHome/details.html', {'project': project, 'images': additionalImages, 'page': 'details'})

def treact(request):
    return render(request, 'portHome/treact.html')
