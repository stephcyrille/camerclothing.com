from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Product, Category, Collection, Catalogue


def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:
		products = Product.objects.filter(title__icontains=q)
		collections = Collection.objects.all()
		catalogues = Catalogue.objects.all()
		context = {'query': q, 'products': products, "collections":collections, "catalogues": catalogues}
		template = 'products/results.html'
	else:
		template = 'products/home.html'
		collections = Collection.objects.all()
		catalogues = Catalogue.objects.all()
		context = {"collections":collections, "catalogues": catalogues}
	return render(request, template, context)


def home(request):
	template = 'products/home.html'
	chaussures_femme = Product.objects.filter(catalogue__slug="femmes", category__slug="ballerines").order_by('?')[:4]
	chaussures = Product.objects.filter(timestamp__lte=timezone.now(), category__slug="chaussures-de-ville").order_by('?')[:3]
	mandeo = Product.objects.filter(timestamp__lte=timezone.now(), collection__slug="mandeo").order_by('?')[:4]
	wax = Product.objects.filter(collection__slug="waxshop").order_by('?')[:3]
	vetMenu = Category.objects.filter(big_cat='VET').order_by('-title')
	chaussuresMenu = Category.objects.filter(big_cat='CHS').order_by('-title')
	accessMenu = Category.objects.filter(big_cat='ACC').order_by('-title')

	vetMenuH = Category.objects.filter(big_cat='VET', catalogue__slug="hommes").order_by('-title')
	chaussuresMenuH = Category.objects.filter(big_cat='CHS', catalogue__slug="hommes").order_by('-title')

	vetMenuF = Category.objects.filter(big_cat='VET', catalogue__slug="femmes").order_by('-title')
	chaussuresMenuF = Category.objects.filter(big_cat='CHS', catalogue__slug="femmes").order_by('-title')

	collections = Collection.objects.all()
	catalogues = Catalogue.objects.all()

	context = {
		'chaussures': chaussures,
		"collections": collections,
		"catalogues": catalogues,
		"vetMenu": vetMenu,
		"vetMenuH": vetMenuH,
		"vetMenuF": vetMenuF,
		"chaussuresMenu": chaussuresMenu,
		"chaussuresMenuH": chaussuresMenuH,
		"chaussuresMenuF": chaussuresMenuF,
		"accessMenu": accessMenu,
		"chaussures_femme": chaussures_femme,
		"mandeo": mandeo,
		"wax": wax,
		}
	return render(request, template, context)



def singleCollection(request, slug):
    collection = get_object_or_404(Collection, slug=slug)
    col = str(collection.slug)

    if col == "mandeo":
        mandeo = col

    elif col == "waxshop":
        wax = col

    elif col == "saphir":
        saphir = col

    elif col == "yvesrocher":
        rocher = col


    catalogues = Catalogue.objects.all()
    collections = Collection.objects.all()

    products = Product.objects.filter(timestamp__lte=timezone.now(), collection__slug=col).order_by('?')[:24]

    template = 'products/colection_single.html'
    return render(request, template, locals())


def singleCatalogue(request, slug):
	catalogue = get_object_or_404(Catalogue, slug=slug)
	catal = str(catalogue.slug)

	name = catal

	collections = Collection.objects.all()

	catalogues = Catalogue.objects.all()

	if catal == "hommes":
		pulls = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="pulls-hommes").order_by('?')[:6]
		hauts = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="hauts-hommes").order_by('?')[:6]
		polos = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="polos").order_by('?')[:6]
		chemises = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="chemises").order_by('?')[:6]
		ensembles = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="ensembles-homme").order_by('?')[:6]
		jeans = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="jeans-hommes").order_by('?')[:6]
		vestes = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="vestes-hommes").order_by('?')[:6]
		pantalons = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="pantalons").order_by('?')[:6]
		sv = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="sous-vetements").order_by('?')[:6]
		costumes = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="costumes").order_by('?')[:6]
		cdv = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="chaussures-de-ville").order_by('?')[:6]
		culottes = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="culotte_h").order_by('?')[:6]
		mocassins = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="mocassins-hommes").order_by('?')[:6]
		shorts = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="shorts-hommes").order_by('?')[:6]
		accessoires = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="accessoires-homme").order_by('?')[:6]
		casquettes = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="casquettes").order_by('?')[:6]
		tennis = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="tennis").order_by('?')[:6]

		vets = Category.objects.filter(big_cat='VET', catalogue__slug="hommes").order_by('-title')
		chs = Category.objects.filter(big_cat='CHS', catalogue__slug="hommes")
		access= Category.objects.filter(big_cat='ACC', catalogue__slug="hommes")

		template = 'products/catalogues/catalogue_hommes.html'

		return render(request, template, locals())


	elif catal == "femmes":
		ballerines = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="ballerines").order_by('?')[:6]
		hauts = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="hauts-femmes").order_by('?')[:6]
		chemisiers = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="chemisiers").order_by('?')[:6]
		robes = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="robes").order_by('?')[:6]
		jupes = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="jupes").order_by('?')[:6]
		jeans = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="jeans-femmes").order_by('?')[:6]
		pantalons_leggins = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="pantalons-et-leggins").order_by('?')[:6]
		pulls = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="pulls-femmes").order_by('?')[:6]
		vestes = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="vestes-femmes").order_by('?')[:6]
		lingerie = Product.objects.filter(timestamp__lte=timezone.now(), catalogue__slug=catal, category__slug="lingerie").order_by('?')[:6]

		vets = Category.objects.filter(big_cat='VET', catalogue__slug="femmes").order_by('-title')
		chs = Category.objects.filter(big_cat='CHS', catalogue__slug="femmes")
		access= Category.objects.filter(big_cat='ACC', catalogue__slug="femmes")

		template = 'products/catalogues/catalogue_femmes.html'

		return render(request, template, locals())


	elif catal == "enfants":
		accessoires = None
		chemises = None
		chaussures = None
		debardeurs = None
		jeans = None
		polos = None
		vestes = None
		pantalons = None
		pulls = None
		sv = None
		teech = None


		chs = Category.objects.filter(big_cat='CHS', catalogue__slug="enfants")
		access= Category.objects.filter(big_cat='ACC', catalogue__slug="enfants")

		template = 'products/catalogues/catalogue_enfants.html'

		vets = Category.objects.filter(big_cat='VET', catalogue__slug="enfants").order_by('-title')
		return render(request, template, locals())

	else:
		print ("Erreur 404") # erreur 404

def singleCat(request, slug):
    category = get_object_or_404(Category, slug=slug)
    cat = str(category.slug)
    catal = str(category.catalogue)
    products = Product.objects.filter(timestamp__lte=timezone.now(), category__slug=cat).order_by('?')[:16]

    if catal == "hommes":
        vets = Category.objects.filter(big_cat='VET', catalogue__slug="hommes").order_by('-title')
        chs = Category.objects.filter(big_cat='CHS', catalogue__slug="hommes")
        access= Category.objects.filter(big_cat='ACC', catalogue__slug="hommes")

        collections = Collection.objects.all()

        catalogues = Catalogue.objects.all()

        template = "products/category/single.html"
        return render(request, template, locals())

    elif catal == "femmes":
        vets = Category.objects.filter(big_cat='VET', catalogue__slug="femmes").order_by('-title')
        chs = Category.objects.filter(big_cat='CHS', catalogue__slug="femmes")
        access= Category.objects.filter(big_cat='ACC', catalogue__slug="femmes")

        collections = Collection.objects.all()

        catalogues = Catalogue.objects.all()

        template = "products/category/single.html"
        return render(request, template, locals())

    elif catal == "enfants":
        vets = Category.objects.filter(big_cat='VET', catalogue__slug="enfants").order_by('-title')
        chs = Category.objects.filter(big_cat='CHS', catalogue__slug="enfants")
        access= Category.objects.filter(big_cat='ACC', catalogue__slug="enfants")

        collections = Collection.objects.all()

        catalogues = Catalogue.objects.all()

        template = "products/category/single.html"
        return render(request, template, locals())

    else:
        print("Krrkrkrkrkrkrkrkrkrkrr")



def single(request, slug):
	product = get_object_or_404(Product, slug=slug)
	cat = str(product.category.slug)
	products = Product.objects.filter(timestamp__lte=timezone.now(), category__slug=cat).order_by('?')[:4]

	vetMenuH = Category.objects.filter(big_cat='VET', catalogue__slug="hommes").order_by('-title')
	chaussuresMenuH = Category.objects.filter(big_cat='CHS', catalogue__slug="hommes").order_by('-title')

	vetMenuF = Category.objects.filter(big_cat='VET', catalogue__slug="femmes").order_by('-title')
	chaussuresMenuF = Category.objects.filter(big_cat='CHS', catalogue__slug="femmes").order_by('-title')

	template = 'products/single.html'

	collections = Collection.objects.all()

	catalogues = Catalogue.objects.all()

	return render(request, template, locals())


def category(request, slug):
	category = get_object_or_404(Category, slug=slug)

	collections = Collection.objects.all()

	catalogues = Catalogue.objects.all()

	template = "produit/category"
	return render(request, template, locals())