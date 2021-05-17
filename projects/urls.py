from django.urls import path

from .import views 

urlpatterns = [
    path('', views.home, name='Home'),
    path('index', views.index, name='Index'),
    path('projects', views.projects, name='Projects'),
    path('project/id/<int:id>', views.project, name='Project')
]