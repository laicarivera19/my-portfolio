from django.shortcuts import render, redirect
from .models import Contact

def contact_view(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return redirect('contact')  # reload page

    return render(request, 'contact/contact.html')