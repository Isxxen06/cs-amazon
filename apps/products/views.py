from rest_framework import viewsets

from .models import Product

from .serializers import ProductSerializer, ProductListSerializer


class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action in 'list':
            return ProductListSerializer
        return self.serializer_class