from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from accounts.models import UserAdress
from carts.models import Cart
from products.models import Collection, Catalogue
from simpleorder.models import ANUAdress

from django.conf import settings
from django.core.mail import send_mail



def confirmation(request):
	idc = request.session['cart_id']
	cart = Cart.objects.get(id=idc)

	items = cart.cartitem_set.all()
	nber = len(items)
	l = []
	init = 0

	while init < nber:
		article = items[init].product.get_ref()
		l.append(article)
		init = init + 1

	articles = str(l)
	if request.user.is_authenticated:
		id_usr = request.user.id
		user = User.objects.get(id=id_usr).get_username()
		addresses = UserAdress.objects.filter(user=request.user)

		message = "camerclothing.com; \nClient : %s; \nAdresse client: %s ;\n\nRef produit(s): %s\n" %(user, addresses, articles)
		send_mail('Commande', message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_TO_EMAIL], fail_silently=False)


	else:
		au = request.session['anu_id']
		addresse = ANUAdress.objects.get(anu_id=au)
		adr = str(addresse.get_address())
		name = str(addresse.get_name())
		telephone = str(addresse.get_tel())
		message = "camerclothing.com ; \nClient : %s; \nAdresse : %s ; \nTelephone client: %s; \n\nRef produit(s): %s\n;" %(name, adr, telephone, articles)
		send_mail(telephone, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_TO_EMAIL], fail_silently=False)


	del request.session['cart_id']
	del request.session['items_total']

	return HttpResponseRedirect(reverse("terminer"))


def about(request):
    collections = Collection.objects.all()
    catalogues = Catalogue.objects.all()
    template = "about.html"
    return render(request, template, locals())
