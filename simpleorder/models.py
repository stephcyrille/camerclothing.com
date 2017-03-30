from django.conf import settings
from django.db import models



class ANUAdress(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None)
	anu_id = models.CharField(max_length=120, default='ABC', unique=True)
	nom = models.CharField(max_length=120)
	telephone =  models.CharField(max_length=120)
	ville = models.CharField(max_length=120)
	quartier = models.CharField(max_length=120)
	secteur = models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.get_address()

	def get_address(self):
		return "%s, %s, %s" %(self.secteur, self.quartier, self.ville)

	def get_tel(self):
		return "%s" %(self.telephone)

	def get_name(self):
		return "%s " %(self.nom)

	class Meta:
		ordering = ['-updated', '-timestamp']