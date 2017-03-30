from django import forms

from .models import ANUAdress


class AnonymUserAddressForm(forms.ModelForm):
	nom = forms.CharField(label="Nom et prenom", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nom'}))
	telephone = forms.CharField(label="Téléphone", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'telephone'}))
	ville = forms.CharField(label="Ville", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'ville'}))
	quartier = forms.CharField(label="Quartier", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'quartier'}))
	secteur = forms.CharField(label="Secteur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'secteur'}))

	class Meta:
		model = ANUAdress
		fields =   ["nom",
					"telephone",
					"ville",
					"quartier",
					"secteur",
					]