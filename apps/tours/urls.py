from rest_framework.routers import DefaultRouter

from .views import TourViewSet, TourCategoryViewSet


router = DefaultRouter()
router.register(r'tours', TourViewSet)
router.register('tours/category', TourCategoryViewSet)

urlpatterns = router.urls
