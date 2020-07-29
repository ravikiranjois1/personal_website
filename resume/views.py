from django.shortcuts import render

# Create your views here.
from resume.models import Resume


def resume_index(request):
      resume_file = Resume.objects.all()
      context = {
          'resume': resume_file
      }
      return render(request, 'resume.html', context)