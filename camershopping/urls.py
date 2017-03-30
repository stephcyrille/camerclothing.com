from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from products import views as productView
from carts import views as cartView
from orders import views as ordersView
from accounts import views as accountsViews
from communication import views as sms
admin.autodiscover()




urlpatterns = [
    url(r'^admin/stephcyrille/camerclothing/admin/', include(admin.site.urls)),

    url(r'^$', productView.home, name='home'),
    url(r'^s/$', productView.search, name='search'),
    url(r'^about/$', sms.about, name="contact"),

    url(r'^categorie/(?P<slug>[\w-]+)/$', productView.singleCat , name='category_single'),
    url(r'^collection/(?P<slug>[\w-]+)/$', productView.singleCollection , name='collection_single'),
    url(r'^catalogue/(?P<slug>[\w-]+)/$', productView.singleCatalogue , name='catalogue_single'),

    url(r'^produits/(?P<slug>[\w-]+)/$', productView.single, name='single_product'),

    url(r'^cart/(?P<id>\d+)/$', cartView.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', cartView.add_to_cart, name='add_to_cart'),
    url(r'^cart/$', cartView.view, name='cart'),

    url(r'^startorder/$', ordersView.startorder, name='startorder'),

    url(r'^commander_one/$', ordersView.checkout_one, name='checkout_one'),
    url(r'^commander/$', ordersView.checkout, name='checkout'),
    url(r'^commander/message/$', sms.confirmation, name='confirmation'),

    url(r'^commander/guess/',include('simpleorder.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/address/add/$', accountsViews.add_user_address, name='add_user_address'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

