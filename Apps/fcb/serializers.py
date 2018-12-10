from rest_framework import serializers
from Apps.fcb.models import Player


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'