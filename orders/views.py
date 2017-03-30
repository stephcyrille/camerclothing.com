from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from accounts.models import UserAdress
from carts.models import Cart

from .models import Order
from .utils import id_generator




def startorder(request):
	template = "startorder.html"
	return render(request, template, locals())


@login_required(login_url='/accounts/login/')
def checkout_one(request):
	addresses = UserAdress.objects.filter(user=request.user)

	context = {
	"addresses": addresses,
	}
	template = "orders/checkout_one.html"
	return render(request, template, context)



@login_required(login_url='/accounts/login/')
def checkout(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
		#return HttpResponseRedirect("/cart/")
		return HttpResponseRedirect(reverse("cart"))

	try:
		new_order = Order.objects.get(cart=cart)
	except Order.DoesNotExist:
		new_order = Order()
		new_order.cart = cart
		new_order.user = request.user
		new_order.order_id = id_generator()
		new_order.save()
	except:
		new_order = None
		# work on some error message
		return HttpResponseRedirect(reverse("cart"))

	if new_order is not None:
		new_order.sub_total = cart.total
		new_order.save()


		addresses = UserAdress.objects.filter(user=request.user)

	context = {
	"order": new_order,
	"addresses": addresses,
	}
	template = "orders/checkout.html"
	return render(request, template, context)






