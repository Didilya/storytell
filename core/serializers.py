from rest_framework import serializers
from users.serializers import UserSerializer
from core import models
import logging

logger = logging.getLogger(__name__)


class TopicListSerializer(serializers.ListSerializer):
    entry_count = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = models.Topic
        fields = ["user", "title", "created", "entry_count"]


class TopicSerializer(serializers.ModelSerializer):
    entry_count = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = models.Topic
        fields = ["user", "title", "created", "entry_count"]
        list_serializer_class = TopicListSerializer

    def get_entry_count(self, obj):
        try:
            if obj.entry_count != 0:
                return obj.entry_count
            else:
                return ""
        except:
            return None


class EntrySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Entry
        fields = ["user", "topic", "text", "created"]


class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Favorite
        fields = ["user", "entry", "created"]


class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Favorite
        fields = ["user", "entry", "is_good", "is_bad", "created"]
