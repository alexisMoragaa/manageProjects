from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Projects(models.Model):
    name = CharField(max_length = 50)
    description = TextField()
    created_at = DateTimeField(auto_now_add = True)
    update_at = DateTimeField(auto_now = True)


class Columns(models.Model):
    name = CharField(max_length = 50)
    description = TextField()
    project_id = ForeignKey(Projects, on_delete = models.CASCADE)
    created_at = DateTimeField(auto_now_add = True)
    updated_at =  DateTimeField(auto_now = True)


class Cards(models.Model):
    title =  CharField(max_length = 100)
    description = TextField()
    column_id = ForeignKey(Columns, on_delete = models.CASCADE)
    created_at = DateTimeField(auto_now_add = True)
    updated_at = DateTimeField(auto_now = True)