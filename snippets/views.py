from django.shortcuts import render
from django.http import HttpResponse JsonResponse
from django.views.decorators import csrf_exempt
from rest_framework.parsers import JSONParser
from . import serializers, models
# Create your views here.

@csrf_exempt
def snippet_list(request):
    """
    List all the code snippets or create
    new code snippets
    """
    if request.method == 'GET':
        snippets = models.Snippets.objects.all()
        serializer = serializers.SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data)
    if request.method == 'POST':
         data = JSONParser().parse(requset)
         serializer = serializers.SnippetSerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data, status=201)
         return JsonResponse(serializer.errors, status=400)
          
