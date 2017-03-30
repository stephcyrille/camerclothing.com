from django import forms
from django.forms import ModelForm, CharField
from django.contrib.auth.hashers import make_password,is_password_usable,check_password
import string
import random
from django.forms import BaseModelFormSet
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import MinimumLengthValidator, validate_password, password_validators_help_text_html
from django.shortcuts import render,redirect
from datetime import *
from django.http import HttpResponseRedirect, HttpResponse,QueryDict


class SignupForm(ModelForm):
	username = forms.CharField(label="Pseudo ",required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name:':'username'}))
	password = forms.CharField(label="Mot de Passe", widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
	verify_password = forms.CharField(label="Vérification Mot de Passe ",widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=100)
	class Meta:
		model = User
		fields = ['username','password','verify_password','email']
		widgets = {
			'email':forms.TextInput(attrs={'class': 'form-control'}),
		}
	def clean(self):
		#rewriting clean method to check whether passwords match or not
		cleaned_data=super(SignupForm,self).clean()
		username=cleaned_data.get('username')
		email=cleaned_data.get('email')
		ps1=cleaned_data.get('password')
		ps2=cleaned_data.get('verify_password')
		if email=="":
			self.add_error('email',"Veuillez ajouter votre email!")
		if ps1!=ps2:
			msg="Les mots de passe ne correspondent pas!"
			self.add_error('verify_password',msg)
		# Save hashed password instead of password directly
		encoded_password=make_password(ps1,make_salt())
		cleaned_data['password']=encoded_password
		# Make sure email is unique
		if email and User.objects.filter(email=email).exclude(username=username).count():
			msg="Email deja pris"
			self.add_error('email',msg)
		# Validate password
		if ps1:
			try:
				validate_password(ps1,user=self)
				cleaned_data['help_text']=None
			except ValidationError:
				cleaned_data['help_text']=password_validators_help_text_html()
				self.add_error('password','Your password it too weak. Please choose another password')
		return cleaned_data


class SigninForm(forms.Form):
	username = forms.CharField(label="Pseudo ",required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'name:':'username'}))
	password = forms.CharField(label="Mot de Passee ", widget=forms.PasswordInput(attrs={'class': 'form-control', 'name':'password'}), max_length=100, )
	def clean(self):
		cleaned_data=super(SigninForm,self).clean()
		username=cleaned_data.get("username")
		password=cleaned_data.get("password")
		if not (username or email):
			msg="Veuillez inserer votre pseudo"
			self.add_error('username',msg)
		lookup=None
		if username:
			if User.objects.filter(username=username).count()==0:
				msg="Nom d'utilisateur non valide!"
				self.add_error('username',msg)
			elif not authenticate(username=username,password=password):
				msg="Le pseudo et mot de passe ne correspondent pas!"
				self.add_error('password',msg)
		return cleaned_data



def make_salt():
    ###Your code here
	letters=string.ascii_letters
	result=random.sample(letters,5)
	return ''.join(result)



