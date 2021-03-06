from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response 
from . import serializers, models
# Create your views here.

class SnippetList(APIView):
    """
    List all snippets or create a new snippet
    """

    def get(self, request, format=None):
        snippets = models.Snippet.objects.all()
        serializer = serializers.SnippetSerializer(snippets,
                        many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.SnippetSerializer(
                        data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete snippet instance.
    """

    def get_object(self, pk):
        try:
            return models.Snippet.objects.get(pk=pk)
        except models.Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        serializer = serializers.SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk=pk)
        serializer = serializers.SnippetSerializer(
                        snippet, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
