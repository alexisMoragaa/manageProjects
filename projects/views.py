from projects.models import Column, Project
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('este es el index')


def home(request):
    return render(request,'Home.html')


def projects(request):
    """Return all projects createds in database"""
    projects = { 'projects' :  Project.objects.all() }
    return render(request, 'Projects.html', projects)


def project(request, id):
    data = {'project' : Project.objects.get(pk = id), 'columns': Column.objects.filter(project = id)}
    # return HttpResponse(data.project)
    return render(request, 'Project.html', data)