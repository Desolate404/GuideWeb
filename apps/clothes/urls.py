from rest_framework.routers import DefaultRouter
from .views import ClothingViewSet, ClothingCategoryViewSet


router = DefaultRouter()
router.register('clothes', ClothingViewSet)
router.register('clothes/category', ClothingCategoryViewSet)

urlpatterns = router.urls
