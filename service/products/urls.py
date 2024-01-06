from django.urls import path
from .views import MainPageDataApiView, Catalog, CatalogDataAPIView, CatalogsInfoAPIView, DiscountedProductListView, \
    NewProductListView, BestSellerListView

urlpatterns = [
    path('home_page_data/', MainPageDataApiView.as_view()),
    path('catalogs_info/', CatalogsInfoAPIView.as_view()),
    path('catalog_data/<slug:slug>', CatalogDataAPIView.as_view()),

    path('discounted_products/', DiscountedProductListView.as_view()),
    path('new_products/', NewProductListView.as_view()),
    path('best_sellers/', BestSellerListView.as_view()),
]
