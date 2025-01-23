from django.views import View
from django.shortcuts import render, redirect
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import *

from django.views.generic import ListView, DetailView, UpdateView, CreateView, RedirectView, DeleteView





def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action', action)
    print('productId', productId)

    product = Product.objects.get(product_id=productId)
    cart, created = Cart.objects.get_or_create(user= request.user)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)


    if action == 'add':
        cartItem.quantity = (cartItem.quantity + 1)
    if action == "remove":
        cartItem.quantity = (cartItem.quantity - 1)

    cartItem.save()

    if cartItem.quantity <= 0:
        cartItem.delete()

    return JsonResponse('Item updated', safe=False)


def cartPage(request):
    print('inside cart page')
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cartItems = cart.items.all()

    else:
        order = {'total_price': 0}
        cartItems = order['total_price']

    context = {"cartItems": cartItems, "cart": cart}
    return render(request, 'cart/cart_list1.html', context)

# def cartPage(request):
#     print('inside cart page')
#     if request.user.is_authenticated:
#         wholesaler = request.user.wholesaler
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         order, created = Order.objects.get_or_create(cart=cart, wholesaler=wholesaler)
#         items = order.items.all()
#         print('Items', items)
#         cartItems = order.get_cart_items
#         print('cartItems',cartItems)
#     else:
#         items = []
#         order = {'calculate_total':0, 'get_cart_items': 0}
#         cartItems = order['get_cart_items']
#
#     context = {'items': items, 'orders': order, "cartItems": cartItems}
#     return render(request, 'cart/cart_list.html', context)





