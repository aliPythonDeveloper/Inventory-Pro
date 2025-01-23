from django.urls import path
from ..views.supplier import SupplierRegisterView

urlpatterns = [
    path('supplier-register/', SupplierRegisterView.as_view(), name ='supplier-register'),

]
