from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

from fournisseur.models import Fournisseur



CHOIX_CATALOGUE = (
					("HOMMES", "Hommes"),
					("FEMMES", "Femmes"),
					("ENFANTS", "Enfants"),
				)

CHOIX_CAT = (
					("VET", "Vêtements"),
					("CHS", "Chaussures"),
					("ACC", "Accessoires"),
				)

class Catalogue(models.Model):
	title = models.CharField(max_length=200, choices=CHOIX_CATALOGUE)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.slug

	def get_image_url(self):
		img = self.imagecatalogue_set.first()
		if img:
			return img.image.url
		return img

	def get_absolute_url(self):
		return reverse("catalogue_single", kwargs={"slug": self.slug})


def image_du_catalogue(instance, filename):
	titre = instance.catalogue.nom
	slug = slugify(titre)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "catalogue/%s/%s" %(slug, new_filename)


class ImageCatalogue(models.Model):
	catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=image_du_catalogue)
	maj = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.catalogue.nom



class Category(models.Model):
	title = models.CharField(max_length=120)
	big_cat = models.CharField(max_length=3, choices=CHOIX_CAT, null=True, blank=True)
	catalogue = models.ForeignKey(Catalogue, blank=True, null=True, on_delete=models.CASCADE)

	slug = models.SlugField(unique=True)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	def get_image_url(self):
		img = self.categoryimage_set.first()
		if img:
			return img.image.url
		return img

	def get_absolute_url(self):
		return reverse("category_single", kwargs={"slug": self.slug})



def category_image(instance, filename):
	titre = instance.category.title
	slug = slugify(titre)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "categorie/%s/%s" %(slug, new_filename)


class CategoryImage(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=category_image)

	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.category.title




CHOIX_COL = (
					("MANDEO", "mandeo"),
					("WAXSHOP", "waxshop"),
					("SAPHIR", "saphir"),
					("YVES ROCHER", "yvesrocher"),
				)

class Collection(models.Model):
	title = models.CharField(max_length=20, choices=CHOIX_COL, null=True, blank=True)
	slug = models.SlugField(unique=True)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	def get_image_url(self):
		img = self.collectionimage_set.first()
		if img:
			return img.image.url
		return img

	def get_absolute_url(self):
		return reverse("collection_single", kwargs={"slug": self.slug})



def collection_image(instance, filename):
	titre = instance.collection.title
	slug = slugify(titre)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "collection/%s/%s" %(slug, new_filename)


class CollectionImage(models.Model):
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=collection_image)

	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.collection.title


class Product(models.Model):
	fournisseur = models.ForeignKey(Fournisseur, null=True)
	title = models.CharField(max_length=120)
	collection = models.ForeignKey(Collection, blank=True, null=True, on_delete=models.CASCADE)
	taille = models.CharField(max_length=120, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	price = models.IntegerField()
	sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)

	catalogue = models.ForeignKey(Catalogue, blank=True, null=True, on_delete=models.CASCADE)

	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	canvas = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	update_defaults = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("single_product", kwargs={"slug": self.slug})

	def get_image_url(self):
		img = self.productimage_set.first()
		if img:
			return img.image.url
		return img

	def get_ref(self):
		return "Article: %s -- Fournisseur: %s -- Prix: %s ;" % (self.title, self.fournisseur, self.price)



def product_image(instance, filename):
	titre = instance.product.title
	slug = slugify(titre)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" %(slug, instance.id, file_extension)
	return "product/%s/%s" %(slug, new_filename)


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=product_image)
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.product.title



class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')

	def colors(self):
		return self.all().filter(category='color')


VAR_CATEGORIES = (
	('size', 'size'),
	('color', 'color'),
	('package', 'package'),
	)


class Variation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	title = models.CharField(max_length=120)
	image = models.ForeignKey(ProductImage, null=True, blank=True, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	objects = VariationManager()

	def __str__(self):
		return self.title

