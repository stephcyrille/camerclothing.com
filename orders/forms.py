from django import forms

from .models import UserAdress


class UserAddressForm(forms.ModelForm):
	class Meta:
		model = UserAdress
		fields = ["addresse", 
					"ville", 
					"region", 
					"pays",
					"telephone"]
