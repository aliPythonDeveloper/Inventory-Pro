from django.urls import path
from ..views.product import *

urlpatterns = [
    path('list/', ProductModelListView.as_view(), name ='list'),
    path('filters/', ProductDRSListView.as_view(), name ='filters'),
    path('product-create/', ProductModelCreateView.as_view(), name='product-create'),
    path('update-product-quantity/', UpdateProduct, name='update-product-quantity'),
    path('<slug:product_slug>/product-update/', ProductModelUpdateView.as_view(), name='product-update'),
    path('<slug:product_slug>/product-detail/', ProductDetailView.as_view(), name='product-detail'),
    path('<slug:product_slug>/product-delete/', ProductModelDeleteView.as_view(), name='product-delete'),

]
