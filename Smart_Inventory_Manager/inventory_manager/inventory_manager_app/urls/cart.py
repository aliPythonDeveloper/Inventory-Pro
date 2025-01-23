from django.urls import path
from ..views.cart import *

urlpatterns = [
    path('update-item/', updateItem, name='update-item'),
    path('', cartPage, name='cart-items'),


]
