from rest_framework import generics
from rest_framework import mixins
from . import serializers, models
from django.contrib.auth.models import User
# Create your views here.

class SnippetList(mixins.ListModelMixin,
        mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin, mixins.DestroyModelMixin,
        generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer 

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
