from django.db import models

# Create your models here.

class Resume(models.Model):
    resume_file = models.FilePathField(path='/resume_pdf')