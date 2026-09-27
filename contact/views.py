from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name    = request.POST.get('name')
        email   = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(
            name=name, email=email, message=message)
        messages.success(request, 'Message sent successfully!')
        return redirect('contact')
    return render(request, 'contact/contact.html')