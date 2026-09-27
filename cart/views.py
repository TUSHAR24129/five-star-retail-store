from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from products.models import Product

@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items   = cart.items.select_related('product')
    return render(request, 'cart/cart.html', {'cart': cart, 'items': items})

@login_required
def add_to_cart(request, product_id):
    product      = get_object_or_404(Product, pk=product_id)
    cart, _      = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'{product.name} added to cart!')
    return redirect('products')

@login_required
def remove_from_cart(request, item_id):
    CartItem.objects.filter(pk=item_id, cart__user=request.user).delete()
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    qty  = int(request.POST.get('quantity', 1))
    if qty > 0:
        item.quantity = qty
        item.save()
    else:
        item.delete()
    return redirect('cart')