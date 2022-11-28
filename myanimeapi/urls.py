from django.urls import path
from . import views

urlpatterns = [
    path('allanimelist', views.AllAnimeList.as_view(),name='AllAnimeList'),
    path('createanimelist', views.CreateAnimeList.as_view(),name='CreateAnimeList'),
    path('updateanimelist/<str:pk>', views.UpdateAnimeList.as_view(),name='UpdateAnimeList'),
    path('deleteanimelist/<int:pk>', views.DeleteAnimeList.as_view(),name='DeleteAnimeList'),
]