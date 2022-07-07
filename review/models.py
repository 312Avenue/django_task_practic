from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product


User = get_user_model()

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'Rating from {self.author} to: {self.product}'