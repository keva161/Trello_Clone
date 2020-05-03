from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Kanban
from .serializers import UserSerializer, KanbanSerializer
from rest_framework import generics, mixins


class UserList(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
