from django.shortcuts import render
from rest_framework.response import Response
from .models import MyAnimeList
from .serializer import MyAnimeListSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.

class AllAnimeList(APIView):
    def get(self,request):
        anime_nme = MyAnimeList.objects.all() #complex data
        serializer = MyAnimeListSerializer(anime_nme,many=True)
        return Response(serializer.data)

class CreateAnimeList(APIView):
    def post(self,request):
        serializer = MyAnimeListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            "Messages":"Failed to Create or Add"
        })

class UpdateAnimeList(APIView):
    def put(self,request,pk):
        anime_name = MyAnimeList.objects.get(pk = pk)
        serializer = MyAnimeListSerializer(anime_name,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"message":"Failed to Update"})


class DeleteAnimeList(APIView):   
    def delete(self,request,pk):
        anime_name = MyAnimeList.objects.get(pk=pk)
        anime_name.delete()
        return Response({
            "message":"Success"
        })
        