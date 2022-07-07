from rest_framework import serializers

from .models import Product
from review.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating']


class ProductSerializer(ReviewSerializer, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['rating'] = ReviewSerializer(instance.review.all(), many=True).data
        return rep


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user

        return super().create(validated_data)