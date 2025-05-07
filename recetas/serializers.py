from rest_framework import serializers
from .models import *

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class RecetaIngredienteSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer()

    class Meta:
        model = RecetaIngrediente
        fields = ['ingrediente', 'cantidad']

class RecetaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    ingredientes = RecetaIngredienteSerializer(source='recetaingrediente_set', many=True, read_only=True)

    class Meta:
        model = Receta
        fields = '__all__'

class FavoritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorita
        fields = '__all__'
