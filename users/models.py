from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, TextField
# Create your models here.
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    """Create model to profile"""
    user = models.OneToOneField(User, on_delete = CASCADE)
    number = models.CharField(max_length = 20, blank = True)
    biography = models.TextField(blank = True)
    picture =  models.ImageField(upload_to='./projects/static/img/profile', blank =  True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username