from django.db import models

# Create your models here.
class Contact(models.Model):
    description = models.TextField()
    gitlink = models.TextField()
    linkedinlink = models.TextField()
    email = models.TextField()
    instagram = models.TextField()
    facebook = models.TextField()