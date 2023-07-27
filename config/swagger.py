from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .generator import BothHttpAndHttpsSchemaGenerator


schema_view = get_schema_view(
    openapi.Info(
        title="Back End API",
        default_version="v0.1",
        description="Test",
        terms_of_service="https://yandex.ru/legal/confidential/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)

swaggerurlpatterns = [
    re_path(r"^docs(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
