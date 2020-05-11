# This is a manually created file allegedly to maintain
# this app's own url mapping
# So basically this page maintains what function to run if someone asks for 'this' url

from django.urls import path
from . import views

urlpatterns = [
	path('dhaka/', views.dhaka, name='dhaka')
]

# Check telusko/settings.py for an important note on urlpatterns