from rest_framework import serializers
from .models import Team, Player

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    player= serializers.HyperlinkedRelatedField(
        view_name='player_details',
        many=True,
        read_only=True
    )
    class Meta:
        model = Team
        fields = ('id', 'name', 'location', 'wins', 'losses', 'player')

class PlayerSerializer(serializers.ModelSerializer):
    team= serializers.SlugRelatedField(

        read_only = True,
        slug_field = 'team',
    )
    class Meta:
        model = Player
        fields = ('id', 'team', 'name', 'position', 'age', 'injuries',)