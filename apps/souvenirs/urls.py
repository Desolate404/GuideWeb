from rest_framework.routers import DefaultRouter

from .views import SouvenirCategoryViewSet, SouvenirViewSet


router = DefaultRouter()
router.register('souvenir', SouvenirViewSet)
router.register('souvenir/category', SouvenirCategoryViewSet)


urlpatterns = router.urls
