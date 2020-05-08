from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	# return HttpResponse("Hello World")
	return render(request, 'home.html',{'name':'voldemort'})		# Now where does home.html live?
						# Not your concern because you have updated the settings.py/DIR
						# & thus django knows

def add(request):

	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])
				# You can access those variables declared in home.html through this request object
	res = val1 + val2
	print('Result is {}'.format(res))

	return render(request, 'result.html', {'result':res})