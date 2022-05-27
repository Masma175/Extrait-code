from django.urls import path, include
from rest_framework import renderers
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# from snippets.views import SnippetList, SnippetDetail
# from snippets.views import SnippetHighlight, UserDetail, UserList, api_root, snippet_list, snippet_detail
from .views import SnippetViewSet, UserViewSet, api_root

""" Urls Simple """

# urlpatterns = [
#     path('', api_root),
#     path('snippets/', snippet_list.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail.as_view(), name='snippet-detail'),
#     path('users/', UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
#     path('snippets/<int:pk>', SnippetHighlight.as_view(), name='snippet-highlight')
# ]

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]
# urlpatterns += format_suffix_patterns(urlpatterns)

""" Urls avec les vues viewsets """

# Liaison explicite des viewSets aux URL

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]


""" Utiliation des viewset avec le routeur """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Enregistrement des viewset dans les routers.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippets")
router.register(r'users', views.UserViewSet,basename="users")

# Les urls de l'API sont automatiquement gérés par le routeur.
urlpatterns = [
    path('', include(router.urls)),
]