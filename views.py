from django.shortcuts import render
from rest_framework import generics
from .serializers import TeamSerializer, PlayerSerializer
from .models import Team, Player
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
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



@api_view(['POST'])
def createPlayer(request):
    pk= request.query_params.get('pk')
    chosen_team = Team.objects.get(pk__iexact = pk)
    print(chosen_team)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    new_player=Player( team = chosen_team, name = body['name'], position = body['position'], age = body['age'], injuries = body['injuries'])
    new_player.save()
    return HttpResponse(new_player, content_type='application/json')


# Hardcoded version
#     @api_view(['POST'])
# def createPlayer(request):
#     team_1 = Team.objects.get(pk=1)
#     print(team_1)
#     request.body
#     new_player=Player( team=team_1, name = 'Matt',position = 'player',age = 30,injuries = 'none')
#     new_player.save()
#     player_dict=model_to_dict(new_player)
#     serializer=json.dumps(player_dict)
#     return HttpResponse(serializer, content_type='application/json')