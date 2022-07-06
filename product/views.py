from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializer import ProductSerializer
from .models import Product


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer