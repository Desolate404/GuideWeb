from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, FoodCategoryViewSet


router = DefaultRouter()
router.register('food', FoodViewSet)
router.register('food/category', FoodCategoryViewSet)

urlpatterns = router.urls
