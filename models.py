from __future__ import division
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    wins = models.CharField(max_length=20)
    losses = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete = models.CASCADE, related_name='player')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default = 'player')
    age = models.CharField(max_length=20)
    injuries = models.CharField(max_length=100, default = 'none')
    
    def __str__(self):
        return self.name