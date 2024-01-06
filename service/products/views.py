from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import Catalog, Product
from .serializers import CatalogsInfoSerializer, CatalogDataSerializer, ProductCardSerializer


class MainPageDataApiView(APIView):
    def get(self, request):
        return


class CatalogsInfoAPIView(ListAPIView):
    serializer_class = CatalogsInfoSerializer

    def get_queryset(self):
        return Catalog.objects.filter(parent__isnull=True)


class CatalogDataAPIView(ListAPIView):
    serializer_class = CatalogDataSerializer

    def get_queryset(self):
        return Catalog.objects.filter(parent__isnull=True)


class DiscountedProductListView(ListAPIView):
    queryset = Product.objects.filter(discount_percent__isnull=False)
    serializer_class = ProductCardSerializer


class NewProductListView(ListAPIView):
    queryset = Product.objects.filter(is_new=True)
    serializer_class = ProductCardSerializer


class BestSellerListView(ListAPIView):
    queryset = Product.objects.filter(is_bestseller=True)
    serializer_class = ProductCardSerializer
