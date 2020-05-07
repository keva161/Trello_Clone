from rest_framework import serializers
from rest_framework.relations import StringRelatedField, PrimaryKeyRelatedField

from api.models import User, Board, List, Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['card_name', 'created_at', 'updated_at']

class ListSerializer(serializers.ModelSerializer):
    list_items = CardSerializer(many=True)
    class Meta:
        model = List
        fields = ['list_name', 'created_at', 'updated_at', 'list_items']

class BoardSerializer(serializers.ModelSerializer):
    lists = ListSerializer(many=True)
    class Meta:
        model = Board
        fields = ['board_name', 'created_at', 'updated_at', 'lists']

class UserSerializer(serializers.ModelSerializer):
    created_boards = BoardSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'created_at', 'updated_at', 'created_boards']