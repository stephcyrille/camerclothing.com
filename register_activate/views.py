from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse,QueryDict
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings

from datetime import *
try:
	# For python2
	import urllib2
except ImportError:
	# For python3
	from urllib.request import urlopen

from xml.dom import minidom
from .forms import SignupForm, SigninForm
from django.db.models import Count
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import get_object_or_404

from products.models import Collection, Catalogue



fromaddr=settings.EMAIL_HOST_USER
username="Stephane Cyrille"
password=settings.EMAIL_HOST_PASSWORD


def sign_up(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user_instance=form.save()
			username=request.POST['username']
			password=request.POST['password']
			user=authenticate(username=username,password=password)
			#The user is not active until they activate their account through email
			user.is_active=False
			user.save()
			id=user.id
			email=user.email
			send_email(email,id)
			return render(request,'thankyou.html')
		else:
			return render(request,'sign_up.html',{'form':form})
	else:
		form = SignupForm()
		return render(request,'sign_up.html',{'form':form})


def activate(request):
	id=int(request.GET.get('id'))
	user = User.objects.get(id=id)
	user.is_active=True
	user.save()
	return render(request,'activation.html')


def sign_in(request):
	try:
		next_page = request.GET.get("next")
	except:
		next_page = None

	if request.method=='POST':
		form=SigninForm(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			user=authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:											#Make sure the account is activated
					login(request,user)
					if next_page is not None:
						return HttpResponseRedirect(str(next_page))
					else:
						return redirect('home')

				else:
					return render(request,'ErrorPage.html')
			else:
				return render(request,'ErrorPage.html',{'errormessage':'Utilisateur pas encor confirmé'})
		else:
			collections = Collection.objects.all()
			catalogues = Catalogue.objects.all()

			return render(request,'sign_in.html', locals())
	else:
		collections = Collection.objects.all()
		catalogues = Catalogue.objects.all()
		form=SigninForm()

		return render(request,'sign_in.html', locals())

@login_required(login_url='/accounts/signin/')
def mainpage(request):
	if request.method == 'GET':
		message="Connection réussie."

		collections = Collection.objects.all()
		catalogues = Catalogue.objects.all()
		return render(request,'mainpage.html', locals())
	elif request.method =='POST':
		if request.POST.get("logout"):
			return redirect('register_activate:logout')
		else:
			return redirect('register_activate:thankyou')


def log_out(request):
	logout(request)

	collections = Collection.objects.all()
	catalogues = Catalogue.objects.all()
	return render(request,'log_out.html', locals())


def send_email(toaddr,id):
	text = "Salut!\nVoici le lien pour activer votre compte sur camershopping:\n Bien vouloir copier puis coler le lien dans la barre de lien de votre navigateur\nhttp://www.camerclothing.com/accounts/activation/?id=%s" %(id)
	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	msg = MIMEMultipart('alternative')
	msg.attach(part1)
	subject="Activez votre compte sur camerclothing"
	msg="""\From: %s\nTo: %s\nSubject: %s\n\n%s""" %(fromaddr,toaddr,subject,msg.as_string())
	#Use gmail's smtp server to send email. However, you need to turn on the setting "lesssecureapps" following this link:
	#https://www.google.com/settings/security/lesssecureapps
	server = smtplib.SMTP('smtp.camerclothing.com:587')
	server.ehlo()
	server.starttls()
	server.login(fromaddr,password)
	server.sendmail(fromaddr,[toaddr],msg)
	server.quit()


