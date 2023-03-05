from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from .utils import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from .sms import send_sms
def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order=data['order']
    items=data['items']
    # send_sms()

    products = Product.objects.all
    context = {'products': products, 'cartItems': cartItems}
    return render(request, "customer/index.html", context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, "customer/cart.html", context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    print(context)
    return render(request, "customer/checkout.html", context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)