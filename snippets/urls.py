from django.urls import path, include
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# from snippets.views import SnippetList, SnippetDetail
from snippets.views import SnippetHighlight, UserDetail, UserList, api_root, snippet_list, snippet_detail




urlpatterns = [
    path('', api_root),
    path('snippets/', snippet_list.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail.as_view(), name='snippet-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('snippets/<int:pk>', SnippetHighlight.as_view(), name='snippet-highlight')
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
# router = routers.DefaultRouter()
# router.register(r'list_snippets', SnippetList)
# router.register(r'list_snippets', SnippetDetail)

# urlpatterns = [
#     path('', include('rest_framework.urls', namespace='rest_framework')),
# ]

urlpatterns += format_suffix_patterns(urlpatterns)