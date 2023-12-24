
from rest_framework import serializers

from .models import Product






class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('category','name','image','description','price','sales_number','stock','is_confirm','is_exists',)
