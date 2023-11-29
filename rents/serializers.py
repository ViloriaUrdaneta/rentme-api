# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Car, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    owner = UserSerializer() 
    images = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Car
        fields = '__all__'
    
    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        owner = User.objects.create(**owner_data)
        
        # Creamos el objeto Car asociado con el propietario
        car = Car.objects.create(owner=owner, **validated_data)
        
        return car

