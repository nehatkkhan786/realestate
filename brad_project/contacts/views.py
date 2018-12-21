from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import *

# Create your views here.


def contact(request):
	if request.method == 'POST':
		listing_id = request.POST['listing_id']
		listing = request.POST['listing']
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		realtor_email = request.POST['realtor_email']

		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id )
			if has_contacted:
				messages.error(request, 'You have already made a querry for this listing. ')
				return redirect('/listings/'+listing_id)

		contact = Contact(

			listing_id = listing_id,
			listing = listing, 
			name = name, 
			email = email, 
			phone = phone, 
			message = message, 
			user_id = user_id
			)
		contact.save()
		# Send Email
		send_mail(
			'Property Listing Query', #Subject 
			'Hello' + name +'! There has been querry for' + listing + '. Please sign in to your dashboard for update', #Message here
			'abdulrasid82@yahoo.com', # From email
			['realtor_email'],
			fail_silently = False

			)
		messages.success(request, 'You request has been submitted, a realtor will get back to you soon')
		return redirect('/listings/'+listing_id)


