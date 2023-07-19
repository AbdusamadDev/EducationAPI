from drf_yasg.generators import OpenAPISchemaGenerator

from django.conf import settings


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        if settings.STAGE == "production":
            schema.schemes = ["https", "http"]
        return schema
