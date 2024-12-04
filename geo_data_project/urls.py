from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Data API",
        default_version="v1",
        description="API for uploading and displaying data",
    ),
    public=True,
)

urlpatterns = [
    path('api/', include('geo_app.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
