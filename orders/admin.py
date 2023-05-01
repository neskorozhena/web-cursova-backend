from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "pharmacy",
        "status",
        "delivery_method",
        "customer_phone",
        "paid",
        "created_at",
        "updated_at",
    )
    inlines = [OrderItemInline]


# Register your models here.
admin.site.register(Order, OrderAdmin)
