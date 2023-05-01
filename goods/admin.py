from django.contrib import admin

from goods.models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ("sku", "name", "price", "created_at", "updated_at")


# Register your models here.
admin.site.register(Goods, GoodsAdmin)
