from django.conf.urls import url
from . import views



urlpatterns = [

	url(r'^start$',views.startorder, name='start'),
	url(r'^end/$',views.endorder, name='end'),
	url(r'^merci/$', views.terminer, name='terminer'),
	]
