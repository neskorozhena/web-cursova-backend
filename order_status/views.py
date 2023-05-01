from rest_framework import viewsets, permissions

from order_status.models import OrderStatus
from order_status.serializers import OrderStatusSerializer


class OrderStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
