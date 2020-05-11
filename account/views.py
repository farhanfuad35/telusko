from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth # Okay. You are supposed to find this line from the google next time haha

# Create your views here.

def registration(request):

	print('Hey I am in registration')

	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']

		if password1 == password2:

			print('Passwords matched')

			if User.objects.filter(username=username).exists():
				print('username exists')
				messages.info(request, 'Username taken')

			elif User.objects.filter(email=email).exists():
				print('email exists')
				messages.info(request, 'Email already in use')

			else:
				# Registration to be completed successfully
				print('proceeding to save in the database')
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save()
				return redirect('/account/login/')		# redirect needs a package to be imported

		else:
			print('Passwords didn\'t match')
			messages.info(request, 'Passwords did not match')
		
		return redirect('/account/registration/')
	

	else:
		return render(request, 'registration.html')


def login(request):
	if request.method == 'POST':
		password = request.POST['password']
		username = request.POST['username']

		if not username or not password:
			messages.info(request, 'Please enter the username and password')
			return redirect('/account/login/')

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			# Login completed
			auth.login(request, user)	# This is how to login the user

			print('User login succeeded')
			return redirect('/')
		else:
			# Login failed
			messages.info(request, "Login failed. Please check your username and/or password")
			print('Login failed')
			return redirect('/account/login/')


	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')