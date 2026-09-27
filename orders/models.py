from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',    'Pending'),
        ('processing', 'Processing'),
        ('shipped',    'Shipped'),
        ('delivered',  'Delivered'),
        ('cancelled',  'Cancelled'),
    ]
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total        = models.DecimalField(max_digits=10, decimal_places=2)
    created_at   = models.DateTimeField(auto_now_add=True)

    # Address fields
    full_name    = models.CharField(max_length=100, default='')
    phone        = models.CharField(max_length=20, default='')
    address      = models.TextField(default='')
    city         = models.CharField(max_length=100, default='')
    state        = models.CharField(max_length=100, default='')
    zip_code     = models.CharField(max_length=20, default='')
    
    # Payment
    payment_method  = models.CharField(max_length=20, default='cod')
    payment_status  = models.CharField(max_length=20, default='unpaid')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price    = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def subtotal(self):
        return self.price * self.quantity