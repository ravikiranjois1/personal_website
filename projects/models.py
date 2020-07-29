from django.db import models


# Create your models here.
class Project(models.Model):
    heading = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    url = models.TextField()
    technology = models.CharField(max_length=300)
    image = models.FilePathField(path='/img')