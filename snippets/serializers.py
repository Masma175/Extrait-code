from email.policy import default
from typing_extensions import Required
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    """ Class serializer d'un extrait de code """
    
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(Required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")


    def creat(self, validated_date):
        """ Creation et affichage du code créé après validation des donnéés fournies """

        return Snippet.objects.create(**validated_date)
    
    def update(self, instance, validated_data):
        """ Mise à jour d'un extrait de code existant """

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()

        return instance