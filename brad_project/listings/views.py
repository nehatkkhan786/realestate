from django.shortcuts import render, get_object_or_404
from . models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import *

# Create your views here.


def listings(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published = True)
	paginator = Paginator(listings, 6)
	page = request.GET.get('page')
	page_listings = paginator.get_page(page)


	return render(request, 'listings/listings.html', {'listings': page_listings})

def listing(request, listing_id):
	listing = get_object_or_404(Listing, pk = listing_id)
	return render(request, 'listings/listing.html', {'listing':listing})

def search(request):

	queryset_list = Listing.objects.order_by('-list_date')	

	# For Keyqords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)

	# For City
	if 'city' in request.GET:
		city = request.GET['city']
		if city:
			queryset_list = queryset_list.filter(city__iexact = city)

	# For State
	if 'state' in request.GET:
		state = request.GET['state']
		if state:
			queryset_list = queryset_list.filter(state__iexact = state)

	# For Bedrooms
	if 'bedrooms' in request.GET:
		bedrooms = request.GET['bedrooms']
		if bedrooms:
			queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)
			

	# For Max Price
	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			queryset_list = queryset_list.filter(price__iexact = price)


	return render(request, 'listings/search.html', 
		{

		'bedroom_choices': bedroom_choices, 'price_choices':price_choices, 'state_choices':state_choices, 'listings': queryset_list, 

		'values': request.GET 

		})
























