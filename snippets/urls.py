from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import snippet_list, snippet_detail

urlpatterns = [
    path('snippets/', snippet_list.as_view()),
    path('snippet/<int:pk>/', snippet_detail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)