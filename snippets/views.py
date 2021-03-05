from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from . import serializers, models
# Create your views here.

@api_view(['GET','POST'])
def snippet_list(request):
    """
    List all the code snippets or create
    new code snippets
    """
    if request.method == 'GET':
        snippets = models.Snippet.objects.all()
        serializer = serializers.SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
         data = JSONParser().parse(request)
         serializer = serializers.SnippetSerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data, status=201)
         return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update, delete a code snippet.
    """
    try:
        snippet = models.Snippet.objects.get(pk=pk)
    except models.Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = serializers.SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = serializers.SnippetSerializer(snippet,
                        data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonRespose(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
          
