from rest_framework import serializers
from users.serializers import UserSerializer
from core import models

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ["user", "title", "created"]

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entry
        fields = ["user", "topic", "text", "created"]

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favorite
        fields = ["user", "entry", "created"]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Favorite
        fields = ["user", "entry", "is_good", "is_bad", "created"]
