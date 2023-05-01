from rest_framework import serializers

from goods.models import Goods
from order_status.models import OrderStatus


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['sku', 'name', 'description', 'price', 'created_at', 'updated_at']
