from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    goods = models.ForeignKey('goods.Goods', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total_price = self.goods.price * self.quantity
        super().save(*args, **kwargs)


class Order(models.Model):
    class DeliveryMethod(models.TextChoices):
        SELF = 'SELF', _('Self')
        DELIVERY = 'DELIVERY', _('Delivery')

    order_number = models.AutoField(primary_key=True, editable=False)
    pharmacy = models.CharField(max_length=100)
    status = models.ForeignKey('order_status.OrderStatus', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    delivery_method = models.CharField(choices=DeliveryMethod.choices, max_length=100, default=DeliveryMethod.DELIVERY)
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_phone = models.CharField(max_length=100, blank=True, null=True)
    items = models.ManyToManyField('goods.Goods', through=OrderItem)
    comment = models.TextField(default='', blank=True)
    paid = models.BooleanField(default=False)
    paid_delivery = models.BooleanField(default=False)
    was_paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.order_number} ({self.status.name})"
