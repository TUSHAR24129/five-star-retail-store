from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model   = OrderItem
    extra   = 0
    readonly_fields = ['product', 'quantity', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'full_name', 'total',
                     'status', 'payment_method', 'payment_status', 'created_at']
    list_editable = ['status', 'payment_status']
    list_filter   = ['status', 'payment_method', 'payment_status']
    search_fields = ['user__username', 'full_name', 'phone']
    inlines       = [OrderItemInline]
    readonly_fields = ['user', 'total', 'created_at']