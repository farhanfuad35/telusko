from django.shortcuts import render
from .models import Destination		# You need to import the class first

# Create your views here.

def index(request):

	# dest1 = Destination()
	# dest1.name = 'Dhaka'
	# dest1.desc = 'The city of color'
	# dest1.id = 1
	# dest1.img = 'destination_1.jpg'
	# dest1.price = 2000
	# dest1.offer = False

	# dest2 = Destination()
	# dest2.name = 'Sylhet'
	# dest2.desc = 'The city of Spirit'
	# dest2.id = 2
	# dest2.img = 'destination_2.jpg'
	# dest2.price = 1700
	# dest2.offer = False

	# dest3 = Destination()
	# dest3.name = 'Chittagong'
	# dest3.desc = 'The daughter of the sea'
	# dest3.id = 3
	# dest3.img = 'destination_3.jpg'
	# dest3.price = 1800
	# dest3.offer = True

	# dests = [dest1, dest2, dest3]

	dests = Destination.objects.all()	# Yes that's fuckin it! Amazing. fetches all the objects from the database table "Destination"

	return render(request, 'index.html', {'dests':dests})