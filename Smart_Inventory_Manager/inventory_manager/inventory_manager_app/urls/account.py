from django.urls import path
from ..views.account import *
from ..views.wholesaler import *

urlpatterns = [
    path('login/', loginUser, name ='login'),
    path('logout/', logoutUser, name ='logout'),
    path('login-type/', loginType.as_view(), name ='login-type'),
    path('activate/<uidb64>/<token>', activate, name ='activate'),

]
