from django.http import HttpResponse, JsonResponse # 'JsonResponse'  est utilisé pour créer une réponse JSON
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser# 'JSONParser' converti les données d'une chaîne écrite au format JSON en un objet JSON qui représente la chaîne
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# Create your views here.


@csrf_exempt
def snippet_list(request):
    """ List des tous les extrait de code et creation d'un extrait """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parser(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

