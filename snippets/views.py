from rest_framework import status
from django.http import HttpResponse, JsonResponse # 'JsonResponse'  est utilisé pour créer une réponse JSON
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser# 'JSONParser' converti les données d'une chaîne écrite au format JSON en un objet JSON qui représente la chaîne
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """ List des tous les extrait de code et creation d'un extrait """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PuT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """ Affichage , modification et suppression d'un extrait de code """
    try:
        snippet = Snippet.objects.get(pk=pk)
        if snippet is not None:
            serializer = SnippetSerializer(snippet, many=False)
            return JsonResponse(serializer.data)
    except Snippet.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        data = JSONParser().parser(request)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)