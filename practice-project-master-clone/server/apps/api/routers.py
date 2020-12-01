from rest_framework import routers

from apps.test.viewsets import TestViewSet
from apps.users.viewsets import UserViewSet
from apps.eats.viewsets import ShopViewSet
from apps.eats.viewsets import IngredientViewSet
from apps.eats.viewsets import DishViewSet


router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('users', UserViewSet, basename='user')
router.register('eats', ShopViewSet, basename='eats')
router.register('dishes', DishViewSet, basename='dish')
router.register('ingredients', IngredientViewSet, basename='ingredient')
