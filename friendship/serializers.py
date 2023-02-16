from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')

    def get_avatar(self, inctance):
        if hasattr(inctance, 'profile') and inctance.profile.avatar:
            return inctance.profile.avatar.url
        return ''