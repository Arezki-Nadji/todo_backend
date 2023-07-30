from django.contrib import admin
from django.urls import path, include
from todo.urls import router as todo_router
from rest_framework import routers,permissions
from user_mangement.urls import router as user_mangement_router
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
import private_storage.urls

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="This API is used to manage todos",
        contact=openapi.Contact(email = "arezki.m.nadji96@gmail.com"),
        license=openapi.License(name='BSD License')
    ),
    public = False,
    permission_classes = [permissions.AllowAny]
)

router = routers.DefaultRouter()
router.registry.extend(todo_router.registry)
router.registry.extend(user_mangement_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('dj-rest-auth/',include('dj_rest_auth.urls')),
    re_path('private-media/',include(private_storage.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

