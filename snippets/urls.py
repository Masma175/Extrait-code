from django.urls import path, include
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# from snippets.views import SnippetList, SnippetDetail
from snippets.views import UserDetail, UserList, snippet_list, snippet_detail




urlpatterns = [
    path('snippets/', snippet_list.as_view()),
    path('snippet/<int:pk>/', snippet_detail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view())
]

# router = routers.DefaultRouter()
# router.register(r'list_snippets', SnippetList)
# router.register(r'list_snippets', SnippetDetail)

# urlpatterns = [
#     path('', include('rest_framework.urls', namespace='rest_framework')),
# ]

urlpatterns += format_suffix_patterns(urlpatterns)