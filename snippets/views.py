from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers, models
# Create your views here.

@api_view(['GET','POST'])
def snippet_list(request, format=None):
    """
    List all the code snippets or create
    new code snippets
    """
    if request.method == 'GET':
        snippets = models.Snippet.objects.all()
        serializer = serializers.SnippetSerializer(
                        snippets, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
         serializer = serializers.SnippetSerializer(
                        data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,
                     status.HTTP_201_CREATED)
         return Response(serializer.errors,
                 status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update, delete a code snippet.
    """
    try:
        snippet = models.Snippet.objects.get(pk=pk)
    except models.Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.SnippetSerializer(snippet)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = serializers.SnippetSerializer(snippet,
                        data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Respose(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          
