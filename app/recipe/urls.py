from django.urls import path, include
from recipe import views
from rest_framework.routers import DefaultRouter

"""
URL mapping for the recipe app
"""

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
