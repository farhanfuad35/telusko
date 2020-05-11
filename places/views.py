from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def dhaka(request):
	print('came to handle dhaka request')
	if request.user.is_authenticated:
		print('user is authenticated')
		return render(request, 'dhaka.html/')
	else:
		return redirect('/account/login/')