from rest_framework import serializers

from app_product.models import Product, Category










class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('seller','category','name','image','description','price','sales_number','stock','is_confirm','is_exists',)


class ProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'image',
            'category',
            'description',
            'price',
            'stock',
        )


class ProfileProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'seller',
            'category',
            'name',
            'image',
            'description',
            'price',
            'stock',
        )

        read_only_fileds = (
            'seller',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = (
            'register_date',
        )
