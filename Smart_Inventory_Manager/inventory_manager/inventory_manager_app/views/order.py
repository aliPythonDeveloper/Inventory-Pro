import datetime
import json

from django.views.generic import ListView, DetailView, UpdateView, CreateView, RedirectView, DeleteView
from ..models import *
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect



def OrderSummary(request):
    if request.user.is_authenticated:
        try:
            wholesaler = request.user.wholesaler
        except AttributeError:
            wholesaler = None

        if not wholesaler:
            # Handle the case where the user does not have a wholesaler
            context = {
                'message': 'You do not have a wholesaler, so there is no order for you.'
            }
            return render(request, 'order/order_summary.html', context)

        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()

        # Retrieve or create the order
        order, created = Order.objects.get_or_create(cart=cart, wholesaler=wholesaler)

        total_price = 0

        for cart_item in cart_items:
            # Check if the order already contains this product
            existing_item = OrderItem.objects.filter(order=order, product=cart_item.product).first()

            # Only create a new OrderItem if it doesn't already exist
            if not existing_item:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                )

            total_price += cart_item.total_price

        order.total_price = total_price
        order.save()

        # Pass orders and order items to the template context
        context = {
            'orders': order
        }
        return render(request, 'order/order_summary.html', context)



def processOrder(request):
    try:
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        if request.user.is_authenticated:
            wholesaler = request.user.wholesaler
            cart = Cart.objects.get(user=request.user)

            order, created = Order.objects.get_or_create(cart=cart, wholesaler=wholesaler)
            order.transaction_id = transaction_id
            order.status = "COMPLETED"
            order.save()

            shipment = Shipment.objects.create(
                 order = order,
                recipient_name=data['shipping']['recipient_name'],
                address_line_1=data['shipping']['address_line_1'],
                address_line_2=data['shipping']['address_line_2'],
                # Optional, defaults to an empty string if not provided
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                postal_code=data['shipping']['postal_code'],
                country=data['shipping']['country'],
                phone=data['shipping']['phone']
            )


        else:
            print('User is not logged in..')
        return JsonResponse('Payment Complete!' ,safe=False)
    except Exception as e:
    # Handle unexpected errors
        return JsonResponse({
            'success': False,
            'message': 'An error occurred while processing the order.',
            'error': str(e)
        }, status=500)
