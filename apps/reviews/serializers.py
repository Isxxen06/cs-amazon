from rest_framework import serializers

from .models import Review


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ("id", "user", "product", "comment", "rating", "created_at")