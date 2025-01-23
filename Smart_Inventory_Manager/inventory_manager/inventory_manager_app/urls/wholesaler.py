from django.urls import path
from ..views.wholesaler import WholesalerRegisterView

urlpatterns = [
    path('wholesaler-register/', WholesalerRegisterView.as_view(), name ='wholesaler-register'),

]
