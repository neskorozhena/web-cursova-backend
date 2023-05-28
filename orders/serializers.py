from django.db.models import Sum
from rest_framework import serializers

from goods.serializers import GoodsSerializer
from order_status.serializers import OrderStatusSerializer
from order_status.models import OrderStatus
from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    # goods = GoodsSerializer(read_only=True)
    name = serializers.ReadOnlyField(source='goods.name')
    manufacturer = serializers.ReadOnlyField(source='goods.manufacturer')
    sku = serializers.ReadOnlyField(source='goods.sku')

    class Meta:
        model = OrderItem
        fields = [
            'name',
            'manufacturer',
            'sku',
            'quantity',
            'total_price',
            'created_at'
        ]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    total_price = serializers.SerializerMethodField()
    status = OrderStatusSerializer(read_only=True)
    items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "order_number",
            "pharmacy",
            "status",
            "payment_method",
            "delivery_method",
            "delivery_price",
            "customer_phone",
            "total_price",
            "items",
            "comment",
            "paid",
            "paid_delivery",
            "was_paid_at",
            "created_at",
            "updated_at",
        ]

    def get_total_price(self, obj: Order) -> float:
        return obj.orderitem_set.aggregate(sum=Sum("total_price"))["sum"]


class OrdersSearchSerializer(serializers.Serializer):
    orders = OrderSerializer(many=True)


class ChangeOrderStatusRequest(serializers.Serializer):
    status = serializers.PrimaryKeyRelatedField(queryset=OrderStatus.objects.all(), required=True)
