from rest_framework import serializers
from users.models import User
from sorl.thumbnail import get_thumbnail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile_name", "thumbnail"]

    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):

        return obj.thumbnail.url.replace(
            "/static/", ""
        )  # get_thumbnail(obj.thumbnail, '200x200', crop='center', quality=99).url
