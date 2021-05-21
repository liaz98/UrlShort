from rest_framework import serializers
from .models import UrlData


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlData
        fields=['new_url', 'url']
        extra_kwargs={
            'url':{'write_only':True},
            'new_url':{'read_only':True}
        }