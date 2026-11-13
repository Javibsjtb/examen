from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["id", "nombre", "especie", "raza", "edad", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
