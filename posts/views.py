from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import PostSerializer, UserSerializer


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# AllowAny
# IsAuthenticated
# IsAdminUser
# IsAuthenticatedOrReadOnly

# WWW-Authenticate: Basic
# WWW-Authenticate: Token

#  Authorization: Basic credential
# btoa - js
# atob - js

# session authenticated
# sesja to record w bazie danych
# request -> do bazy nie znamy wiec tworzona jest sesja
# dajemy mu cookies
# i teraz przegladarka wysyla cookies
# a my sprawdzamy jakie cookies ktos ma
# cookies musi byc trzymany na front i backend

# Cookies HTTP-only - nie da sie modyfikowac JS

# token authentication
