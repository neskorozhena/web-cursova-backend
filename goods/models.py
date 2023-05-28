import uuid

from django.db import models


class Goods(models.Model):
    sku = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=500)
    manufacturer = models.CharField(max_length=500, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Goods"

    def __str__(self):
        return f"({str(self.sku)[:8]}) {self.name}"
