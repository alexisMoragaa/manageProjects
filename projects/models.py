#Django
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.




class Project(models.Model):
    """Create moedel to save projects"""
    name = CharField(max_length = 50)
    description = TextField()
    user = ForeignKey(User, on_delete= models.CASCADE)
    created_at = DateTimeField(auto_now_add = True)
    updated_at = DateTimeField(auto_now = True)

    def __str__(self):
        return self.name



class Column(models.Model):
    """Create model to save columns in projects"""
    name = CharField(max_length = 50)
    description = TextField()
    project = ForeignKey(Project, on_delete = models.CASCADE)
    user = ForeignKey(User, on_delete= models.CASCADE)
    created_at = DateTimeField(auto_now_add = True)
    updated_at =  DateTimeField(auto_now = True)

    def __str__(self) :
            return  '{}   [by @{}]'.format(self.name, self.project)



class Card(models.Model):
    """Create models to save task in columns"""
    title =  CharField(max_length = 100)
    description = TextField()
    column = ForeignKey(Column, on_delete = models.CASCADE)
    user = ForeignKey(User, on_delete= models.CASCADE)
    created_at = DateTimeField(auto_now_add = True)
    updated_at = DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.title

