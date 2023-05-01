from django.contrib import admin

from order_status.models import OrderStatus


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "color", "delivery", "created_at", "updated_at")


# Register your models here.
admin.site.register(OrderStatus, OrderStatusAdmin)
