from django.shortcuts import render, redirect
from products.models import Product

def home_view(request):
    featured_products = Product.objects.filter(stock__gt=0)[:4]
    return render(request, 'home.html',
                  {'featured_products': featured_products})

def about_view(request):
    team = [
        {'name': 'Jackline',  'role': 'Store Manager',        'initial': 'J', 'color': '#2563eb'},
        {'name': 'Srijan',    'role': 'Customer Support Lead', 'initial': 'S', 'color': '#16a34a'},
        {'name': 'Tushar',    'role': 'Product Specialist',    'initial': 'T', 'color': '#9333ea'},
        {'name': 'Sanja',     'role': 'Assistant Manager',     'initial': 'S', 'color': '#dc2626'},
        {'name': 'Manish',    'role': 'Marketing Specialist',  'initial': 'M', 'color': '#ea580c'},
    ]
    return render(request, 'about.html', {'team': team})