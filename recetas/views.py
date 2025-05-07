from rest_framework import viewsets, filters

from recetas.serializers import CategoriaSerializer, FavoritaSerializer, IngredienteSerializer, RecetaSerializer
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'descripcion']

    @action(detail=False, methods=['get'])
    def buscar_por_ingredientes(self, request):
        ingredientes = request.GET.getlist('ingredientes')
        recetas = Receta.objects.filter(
            recetaingrediente__ingrediente__nombre__in=ingredientes
        ).distinct()
        serializer = self.get_serializer(recetas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def filtrar(self, request):
        tiempo = request.GET.get('tiempo')
        dificultad = request.GET.get('dificultad')
        categoria = request.GET.get('categoria')

        recetas = Receta.objects.all()
        if tiempo:
            recetas = recetas.filter(tiempo__lte=tiempo)
        if dificultad:
            recetas = recetas.filter(dificultad=dificultad)
        if categoria:
            recetas = recetas.filter(categoria__nombre=categoria)

        serializer = self.get_serializer(recetas, many=True)
        return Response(serializer.data)

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FavoritaViewSet(viewsets.ModelViewSet):
    queryset = Favorita.objects.all()
    serializer_class = FavoritaSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
