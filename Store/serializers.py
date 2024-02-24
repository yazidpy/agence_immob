from rest_framework import serializers
from . import models


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Property
        fields = '__all__'



class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Apartment
        fields = '__all__'


        
class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Villa
        fields = '__all__'



class GroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ground
        fields = '__all__'


class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Annonce
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile  
        fields = '__all__'

class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.Favoris
        fields='__all__'


class AppartementEstimatorSerializer(serializers.Serializer):
    bedrooms = serializers.FloatField(required=True)
    bathrooms = serializers.FloatField(required=True)
    sqft_living = serializers.FloatField(required=True)
    floors = serializers.FloatField(required=True)
    waterfront = serializers.FloatField(required=True)
    view = serializers.FloatField(required=True)
    condition = serializers.FloatField(required=True)
    price = serializers.FloatField(read_only=True)
