from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

# Creation de nos views
def hello(request):
	bands = Band.objects.all()
	return HttpResponse(f"""
					<h1>Hello Django!</h1>
					<p>Mes groupes preferes sont :</p>
					<ul>
						<li>{bands[0].name}</li>
						<li>{bands[1].name}</li>
					 	<li>{bands[2].name}</li>
					</ul>
					""")

def about(request):
	return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch</p>')

def listings(request):
	return HttpResponse('<h1>Liste de nos articles</h1> <p>Comment trouvez-vous nos articles?</p>')

def contact(request):
	return HttpResponse('<h1>Contactez nous!</h1> <p>Nous sommes joignable 24h/7j</p>')