from rest_framework import serializers
from users.models import User
from sorl.thumbnail import get_thumbnail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile_name", "email", "small_thumbnail"]

    thumbnail = serializers.SerializerMethodField()

    def get_small_thumbnail(self, obj):

        return get_thumbnail(self.thumbnail, '200x200', crop='center', quality=99).url