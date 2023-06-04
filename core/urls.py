from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Backend for Hacaton",
        default_version='v1',
        description="API for Hacaton",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.users.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),

    path('', include('apps.food.urls')),
    path('', include('apps.fourm.urls')),
    path('', include('apps.clothes.urls')),
    path('', include('apps.tours.urls')),
    path('', include('apps.favorites.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
