from rest_framework import serializers
from .models import IAP, Jogo

class IAPSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    jogo = serializers.SerializerMethodField()

    def get_jogo(self, obj):
        return obj.jogo.nome

    class Meta:
        model = IAP
        fields = ['id', 'price', 'jogo']

    def get_id(self, obj):
        return obj.nome  



class JogoSerializer(serializers.ModelSerializer):
    iaps = IAPSerializer(many=True, read_only=True)

    class Meta:
        model = Jogo
        fields = ['id', 'nome', 'iaps']

