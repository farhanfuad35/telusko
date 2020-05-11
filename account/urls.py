# This is a manually created file allegedly to maintain
# this app's own url mapping
# So basically this page maintains what function to run if someone asks for 'this' url

from django.urls import path
from . import views

urlpatterns = [
	path('registration/', views.registration, name='registration'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout')
]

# Check telusko/settings.py for an important note on urlpatterns