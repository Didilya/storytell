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
        fields = ["id", "user", "title", "created", "entry_count"]


class TopicSerializer(serializers.ModelSerializer):
    entry_count = serializers.SerializerMethodField()
    user = UserSerializer()
    uid = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = models.Topic
        fields = ["id", "uid", "user", "title", "created", "entry_count", "url"]
        list_serializer_class = TopicListSerializer

    def get_entry_count(self, obj):
        try:
            if obj.entry_count != 0:
                return obj.entry_count
            else:
                return ""
        except:
            return None

    def get_uid(self, obj):
        return obj.uid.hex

    def get_url(self, obj):
        return f"topics/{obj.uid}/"


class EntrySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    favorite_count = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    uid = serializers.SerializerMethodField()
    page = serializers.SerializerMethodField()

    class Meta:
        model = models.Entry
        fields = [
            "user",
            "uid",
            "topic",
            "text",
            "created",
            "favorite_count",
            "title",
            "page",
        ]

    def get_favorite_count(self, obj):
        try:
            if obj.favorite_count != 0:
                return obj.favorite_count
            else:
                return 0
        except:
            return ""

    def get_page(self, obj):
        return 10

    def get_title(self, obj):
        return self.context.get("title")

    def get_created(self, obj):
        return obj.created.strftime("%d.%m.%Y %H:%M")

    def get_uid(self, obj):
        return obj.uid.hex


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
