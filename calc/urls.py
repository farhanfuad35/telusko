# This is a manually created file allegedly to maintain
# this app's own url mapping
# So basically this page maintains what function to run if someone asks for 'this' url

from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),	# Tells to run the views.home function]
	path('add',views.add, name='add'),	# Once the form is submitted, execute add method in views.py
]