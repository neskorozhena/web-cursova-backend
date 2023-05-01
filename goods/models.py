import uuid

from django.db import models


class Goods(models.Model):
    sku = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Goods"

    def __str__(self):
        return f"({str(self.sku)[:8]}) {self.name}"
