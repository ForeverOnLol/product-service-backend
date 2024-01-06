from rest_framework import serializers
from .models import Catalog, Product


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['title', 'description', 'slug', 'url']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CatalogsInfoSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        fields = ['title', 'description', 'slug', 'children', 'products_count']

    def get_children(self, obj):
        children_qs = Catalog.objects.filter(parent=obj)
        serializer = CatalogsInfoSerializer(children_qs, many=True)
        return serializer.data

    def get_products_count(self, obj):
        products_count = Product.objects.filter(catalog=obj).count()
        return products_count


class CatalogDataSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        fields = ['title', 'description', 'slug', 'children', 'products_count']

    def get_children(self, obj):
        children_qs = Catalog.objects.filter(parent=obj)
        serializer = CatalogSerializer(children_qs, many=True)
        return serializer.data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['catalog']

class MainPageDataSerializer(serializers.ModelSerializer):
    pass