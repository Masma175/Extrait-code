from requests import Response
from django.contrib.auth.models import User
from rest_framework import status, generics
from django.http import Http404, HttpResponse, JsonResponse # 'JsonResponse'  est utilisé pour créer une réponse JSON
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser# 'JSONParser' converti les données d'une chaîne écrite au format JSON en un objet JSON qui représente la chaîne
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
# Create your views here.

""" Vues Basé sur les fonctions """

# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     #""" List des tous les extrait de code et creation d'un extrait """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PuT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     #""" Affichage , modification et suppression d'un extrait de code """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#         if snippet is not None:
#             serializer = SnippetSerializer(snippet, many=False)
#             return JsonResponse(serializer.data)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "PUT":
#         data = JSONParser().parser(request)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         snippet.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


""" Vue basés sur les classes """

# class snippet_list(APIView):
#     """ Affichage , modification et suppression d'un extrait de code """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class snippet_detail(APIView):
#     """ Affichage , modification et suppression d'un extrait de code """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         return Response(serializer.data)
        

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


""" Vuse du model Snippet Avec generics """

class snippet_list(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class snippet_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


""" Vues du model User """

class UserList(generics.ListAPIView):
    """ Vue liste User """
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetail(generics.RetrieveAPIView):
    """ Vue detail User """
    queryset = User.objects.all()
    serializer_class = UserSerializer