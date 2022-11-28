from rest_framework import serializers
from .models import MyAnimeList

class MyAnimeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAnimeList
        fields = '__all__'