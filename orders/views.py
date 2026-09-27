from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import Cart

@login_required
def checkout(request):
    try:
        cart  = Cart.objects.get(user=request.user)
        items = cart.items.select_related('product')
    except Cart.DoesNotExist:
        return redirect('cart')

    if not items.exists():
        messages.error(request, 'Your cart is empty!')
        return redirect('cart')

    total = sum(item.subtotal for item in items)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method', 'cod')

        order = Order.objects.create(
            user           = request.user,
            total          = total,
            full_name      = request.POST.get('full_name'),
            phone          = request.POST.get('phone'),
            address        = request.POST.get('address'),
            city           = request.POST.get('city'),
            state          = request.POST.get('state'),
            zip_code       = request.POST.get('zip_code'),
            payment_method = payment_method,
            payment_status = 'paid' if payment_method == 'card' else 'unpaid',
        )

        for item in items:
            OrderItem.objects.create(
                order    = order,
                product  = item.product,
                quantity = item.quantity,
                price    = item.product.price
            )
            item.product.stock -= item.quantity
            item.product.save()

        cart.items.all().delete()
        messages.success(request, f'Order #{order.id} placed successfully!')
        return redirect('order_list')

    return render(request, 'orders/checkout.html',
                  {'items': items, 'total': total})

@login_required
def order_list(request):
    orders = Order.objects.filter(
        user=request.user).order_by('-created_at')
    return render(request, 'orders/orders.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except Order.DoesNotExist:
        return redirect('order_list')
    return render(request, 'orders/order_detail.html', {'order': order})