from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Animal(models.Model):
    nombre = models.CharField(max_length=80)
    especie = models.CharField(max_length=60)
    raza = models.CharField(max_length=80)
    edad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
