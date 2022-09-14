from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class likedItem(models.Model):
    # what user applied to what object
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # two pieces of info:
    # what object type? product, article, video etc. use abstract model, installed app contenttype. django.contrib.contenttypes
    # what object ID?
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
