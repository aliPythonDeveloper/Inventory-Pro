from django.urls import path
from ..views.order import *

urlpatterns = [
    path('order-summary/', OrderSummary, name='order-summary'),
    path('process-order/', processOrder, name='process-order'),
]
