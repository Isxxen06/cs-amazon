from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import Product

from .serializers import ProductSerializer, ProductListSerializer, ProductDetailSerializer
from .filters import ProductFilter


class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        filters.DjangoFilterBackend
    ]
    filterset_fields = [
        "name"
    ]
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action in 'list':
            return ProductListSerializer
        elif self.action in 'retrieve':
            return ProductDetailSerializer
        return self.serializer_class