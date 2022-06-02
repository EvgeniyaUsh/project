from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(serializers.ModelSerializer):
    # в скрытом поле по умолчанию прописывается текущий пользователь
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        exclude = ('like',)


class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ('id',)
