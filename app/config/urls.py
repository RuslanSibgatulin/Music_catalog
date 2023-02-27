from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views

schema_view = get_schema_view(
    openapi.Info(
        title="Muzcat API",
        default_version="v1"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("apidocs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/v1/", include("albums.urls", namespace="albums_api")),
]