from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.models import Post
from api.permisisions import IsOwnerOrReadOnly
from api.serializers import PostSerializer, PostLikeSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)


class PostLikeViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=request.data['id'])
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)
        post.save()
        count_like = post.likes_counter()
        return Response(data=count_like)
