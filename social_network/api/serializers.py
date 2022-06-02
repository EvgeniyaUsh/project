from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Post


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                        first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')


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
