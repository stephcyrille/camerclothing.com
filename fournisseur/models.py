from django.db import models



class Fournisseur(models.Model):
	nom = models.CharField(max_length=100, null=True)
	prenom = models.CharField(max_length=100, null=True)
	tel = models.CharField(max_length=15, null=True)
	adresse = models.CharField(max_length=250, null=True)
	souscrit = models.BooleanField(default=True)

	def __str__(self):
		return self.nom

