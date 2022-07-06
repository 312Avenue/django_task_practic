from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product


User = get_user_model()

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    rating = models.IntegerChoices('Place', 'Low Normal High Best TheBest')