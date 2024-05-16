from rest_framework import serializers

from data.models import *

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

class ClubListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'title', 'adress']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class PCLevelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCLevel
        fields = ['id', 'title']


class PCLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCLevel
        fields = '__all__'


class PCListSerializer(serializers.ModelSerializer):
    club = ClubListSerializer()
    pc_level = PCLevelListSerializer()

    class Meta:
        model = PC
        fields = '__all__'


class PCSerializer(serializers.ModelSerializer):
    club = ClubSerializer()
    pc_level = PCLevelSerializer()

    class Meta:
        model = PC
        fields = '__all__'