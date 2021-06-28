from projects.models import Column, Project, Card
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
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

    data = {'project' : Project.objects.get(pk = id), 'column': Column.objects.filter(project = id) }

    return render(request, 'Project.html', data)



def tasks(request, idColumn):
    data  = Card.objects.filter(column = idColumn).only('id')
    return HttpResponse(serialize('json', data), 'application/json')
    


