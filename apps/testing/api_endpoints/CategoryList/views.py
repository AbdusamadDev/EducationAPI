from rest_framework.generics import ListAPIView
from apps.testing.models import Category
from apps.testing.api_endpoints.CategoryList.serializers import CategoryListSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


__all__ = ['CategoryListView']
