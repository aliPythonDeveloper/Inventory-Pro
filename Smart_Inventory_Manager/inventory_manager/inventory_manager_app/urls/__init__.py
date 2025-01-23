from django.urls import path, include
from ..views.home import RootUrlView
app_name = "inventory_manager_app"

urlpatterns = [
    path('', RootUrlView.as_view(), name='home'),
    path('account/',include('inventory_manager_app.urls.account')),
    path('cart/', include('inventory_manager_app.urls.cart')),
    path('product/', include('inventory_manager_app.urls.product')),
    path('supplier/', include('inventory_manager_app.urls.supplier')),
    path('wholesaler/', include('inventory_manager_app.urls.wholesaler')),
    path('order/', include('inventory_manager_app.urls.order')),
    path('shipment/', include('inventory_manager_app.urls.shipment')),

]