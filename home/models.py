from django.db import models

# Create your models here.


class Home(models.Model):
    header = models.CharField(max_length=200)
    tag = models.TextField()
    description_1 = models.TextField()
    description_2 = models.TextField()
    description_3 = models.TextField()
    description_4 = models.TextField()
    contact_heading = models.TextField()
    git = models.CharField(max_length=300, default='SOME STRING')
    linkedin = models.CharField(max_length=300, default='SOME STRING')
    email = models.CharField(max_length=300, default='SOME STRING')
    fb = models.CharField(max_length=300, default='SOME STRING')
    insta = models.CharField(max_length=300, default='SOME STRING')
    phone = models.CharField(max_length=300, default='SOME STRING')
    background_1 = models.FilePathField(path='/img', default='SOME STRING')
    background_2 = models.FilePathField(path='/img', default='SOME STRING')
    background_3 = models.FilePathField(path='/img', default='SOME STRING')
    background_4 = models.FilePathField(path='/img', default='SOME STRING')
    background_5 = models.FilePathField(path='/img', default='SOME STRING')
    profile_photo = models.FilePathField(path='/img', default='SOME STRING')