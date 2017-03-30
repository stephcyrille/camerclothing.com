from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect

from carts.models import Cart

from orders.models import Order

from orders.utils import id_generator

from .forms import AnonymUserAddressForm
from .models import ANUAdress



def startorder(request):
	print (request.GET)
	form = AnonymUserAddressForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			new_address = form.save(commit=False)
			request.user = None
			new_address.user = request.user
			new_address.anu_id = id_generator()
			auid = new_address.anu_id
			request.session['anu_id'] = auid
			new_address.save()
			return HttpResponseRedirect('/commander/guess/end/')

	submit_btn = "Sauvegarder addresse"
	form_title = "Ajouter une nouvelle Adresse"
	return render(request, "simpleorder/begining.html",
		{"form": form,
		"submit_btn": submit_btn,
		"form_title": form_title,
		})


def endorder(request):
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
		new_order.order_id = id_generator()
		new_order.save()
	except:
		new_order = None
		# work on some error message
		return HttpResponseRedirect(reverse("cart"))

	if new_order is not None:
		new_order.sub_total = cart.total
		new_order.save()

		au = request.session['anu_id']
		addresses = ANUAdress.objects.get(anu_id=au)


	context = {
				"order": new_order,
				"addresses" : addresses,
				}
	template = "simpleorder/ending.html"
	return render(request, template, context)

def terminer(request):
    template = "simpleorder/merci.html"
    return render(request, template)

