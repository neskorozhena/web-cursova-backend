from rest_framework import viewsets, permissions

from goods.models import Goods
from goods.serializers import GoodsSerializer


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = [permissions.IsAuthenticated]
