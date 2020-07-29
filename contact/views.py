from django.shortcuts import render
from contact.models import Contact


# Create your views here.
def contact_index(request):
    contact_info = Contact.objects.all()
    context = {
        'contact': contact_info
    }
    return render(request, 'contact_index.html', context)