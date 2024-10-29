from rest_framework import serializers
from users.models import User
from sorl.thumbnail import get_thumbnail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile_name", "email", "small_thumbnail"]

    small_thumbnail = serializers.SerializerMethodField()

    def get_small_thumbnail(self, obj):

        return obj.thumbnail.url.replace(
            "/static/", ""
        )  # get_thumbnail(obj.thumbnail, '200x200', crop='center', quality=99).url
