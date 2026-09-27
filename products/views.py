from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    query       = request.GET.get('q', '')
    category_id = request.GET.get('category')
    categories  = Category.objects.all()
    products    = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)
    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'products/products.html', {
        'products':   products,
        'categories': categories,
        'query':      query,
    })# Products App
# Search
