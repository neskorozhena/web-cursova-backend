from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from orders.models import Order
from orders.serializers import (
    OrderSerializer,
    OrdersSearchSerializer,
    ChangeOrderStatusRequest,
)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="q",
                description="Search by order number or ID",
                required=True,
                type=str,
                location="query",
            )
        ],
        responses=OrdersSearchSerializer,
        methods=["GET"],
    )
    @action(detail=False, methods=["get"])
    def search(self, request):
        queryset = self.get_queryset()
        user_query = request.query_params.get("q")
        if user_query is not None:
            queryset = queryset.filter(
                Q(order_number__icontains=user_query)
                | Q(customer_phone__icontains=user_query)
            )
        serializer = OrdersSearchSerializer(
            {"orders": queryset}, context={"request": request}
        )
        return Response(serializer.data)

    @extend_schema(
        parameters=[ChangeOrderStatusRequest],
        request=None,
    )
    @action(detail=True, methods=["put"])
    def status(self, request, pk=None):
        change_status_request = ChangeOrderStatusRequest(data=request.query_params)
        change_status_request.is_valid(raise_exception=True)
        order = self.get_object()
        order.status = change_status_request.validated_data["status"]
        order.save()
        return Response(self.get_serializer(order).data)
