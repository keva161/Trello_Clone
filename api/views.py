from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Board, List, Card
from api.serializers import UserSerializer, BoardSerializer, ListSerializer, CardSerializer


class UserList(APIView):


    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class BoardList(APIView):


    def get(self, request):
        board = Board.objects.all()
        serializer = BoardSerializer(board, many=True)
        return Response(serializer.data)

class ListsList(APIView):


    def get(self, request):
        list = List.objects.all()
        serializer = ListSerializer(list, many=True)
        return Response(serializer.data)

class CardsList(APIView):


    def get(self, request):
        card = Card.objects.all()
        serializer = CardSerializer(card, many=True)
        return Response(serializer.data)
