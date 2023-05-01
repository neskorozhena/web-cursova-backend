from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class GetUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses=UserSerializer,
    )
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
