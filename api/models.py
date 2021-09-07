from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='image', blank=True,null=True)
