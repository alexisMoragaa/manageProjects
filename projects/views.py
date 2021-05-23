from projects.models import Column, Project, Card
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

    data = {'project' : Project.objects.get(pk = id), 'column': Column.objects.filter(project = id) }

    return render(request, 'Project.html', data)





    """
    {
     1: {'id': 1, 'name': 'To Do', 'description': 'Tareas pendientes', 'cards': {<QuerySet [<Card: Primera Tarea>, <Card: Segunda Tarea>]>}}, 
     2: {'id': 2, 'name': 'In Progress', 'description': 'Tareas En Progreso', 'cards': {<QuerySet []>}}, 
     3: {'id': 3, 'name': 'Done', 'description': 'Tareas Finalzadas', 'cards': {<QuerySet []>}}
    }
    """