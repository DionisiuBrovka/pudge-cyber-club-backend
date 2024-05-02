from rest_framework import serializers

from data.models import *

class ClubListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class PCLevelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCLevel
        fields = '__all__'


class PCLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCLevel
        fields = '__all__'


class PCListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = '__all__'


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = '__all__'