from rest_framework import serializers
from .models import User, Kanban


class KanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban


class UserSerializer(serializers.ModelSerializer):
    boards = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'boards')
