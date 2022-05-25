from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import snippet_list, snippet_detail

urlpatterns = [
    path('snippets/', snippet_list),
    path('snippet/<int:pk>/', snippet_detail),
]

urlpatterns += format_suffix_patterns(urlpatterns)