from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns =[
    path('', views.TeamList.as_view(), name="team_list" ),
    path('player', views.PlayerList.as_view(), name = "player_list"),
    path('team/<int:pk>', views.TeamDetail.as_view(), name="team_details"),
    # path('player/<int:pk>', views.PlayerDetail.as_view(), name="player_details"),
    path('player_name', views.getByPlayerName, name="player_details"),
]