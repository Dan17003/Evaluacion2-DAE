from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('recetas', RecetaViewSet)
router.register('ingredientes', IngredienteViewSet)
router.register('categorias', CategoriaViewSet)
router.register('favoritas', FavoritaViewSet)

urlpatterns = router.urls
