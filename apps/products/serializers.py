from rest_framework import serializers

from .models import Product
from apps.images.serializers import ImageSerializer
from apps.reviews.serializers import ReviewSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "name", "image", "category",
                  "price", "currency")


class ProductDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    product_review = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'