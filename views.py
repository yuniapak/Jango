from django.shortcuts import render
from rest_framework import generics
from .serializers import TeamSerializer, PlayerSerializer
from .models import Team, Player
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
# Create your views here.
class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


@api_view(['GET'])
def getByPlayerName(request):
    name = request.query_params.get('name')
    print(name)
    player= Player.objects.filter(name__iexact=name)
    if len(player)>0:
        serializer=serializers.serialize('json', player)
        return HttpResponse(serializer, content_type='application/json')
    else:
        return Response(name, status=400)
