from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from strig.web.models import User
from strig.web.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, url_path="current", methods=["GET"])
    def current_pools(self, request):
        users = User.active.all()
        serializer = self.get_serializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, url_path="closed", methods=["GET"])
    def closed_pools(self, request):
        users = User.closed.all()
        serializer = self.get_serializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    