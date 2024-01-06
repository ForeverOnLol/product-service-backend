from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Catalog, Product
from .serializers import CatalogsInfoSerializer, CatalogDataSerializer, ProductCardSerializer


class MainPageDataApiView(APIView):
    def get(self, request):
        # Получаем информацию о каталогах
        catalogs_info = CatalogsInfoAPIView().get_queryset()
        catalogs_info_data = CatalogsInfoAPIView.serializer_class(catalogs_info, many=True).data

        # Получаем новые товары
        new_products = NewProductListView().get_queryset()
        new_products_data = ProductCardSerializer(new_products, many=True).data

        # Получаем лидеров продаж
        best_sellers = BestSellerListView().get_queryset()
        best_sellers_data = ProductCardSerializer(best_sellers, many=True).data

        # Получаем товары со скидками
        discounted_products = DiscountedProductListView().get_queryset()
        discounted_products_data = ProductCardSerializer(discounted_products, many=True).data

        # Формируем JSON-ответ
        response_data = {
            'catalogs': catalogs_info_data,
            'new_products': new_products_data,
            'bestseller_products': best_sellers_data,
            'discount_products': discounted_products_data,
        }

        return Response(response_data)


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
