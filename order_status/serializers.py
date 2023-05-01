from rest_framework import serializers

from order_status.models import OrderStatus


class OrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['code', 'name', 'color', 'delivery', 'created_at', 'updated_at']
