from django.urls import path
from .views import ProductDetailView, product_list

urlpatterns = [
    # path(
    #     'products/',
    #     ProductListView.as_view(),
    #     name='product_list'),
    path("products/", product_list, name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
