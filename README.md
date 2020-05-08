# telusko
A python Django project inspired by a youtube channel called telusko

1. First create a virtual environment
	pipenv shell
2. Install django
	pipenv install django
3. Create a project
	django-admin startproject [project_name]
4. Run Server
	python manage.py runserver
5. Create an app
	python manage.py startapp [app_name]
6. Create urls.py in the app directory to create the sitemap from there
7. In urls.py/url pattern: set the path and tell it to run which function. Here views.hello()

8. Update original urls.py to refer to the newly created app's urls.py

9. To show a template html, Change TEMPLATES section in the settings.py. Add template to the DIR section

10. Update views.py

11. Use a base html page. Use a section to be referred by other specific html code (home.html in this case)

12. Use a simple HTML form to take two numbers as input and print the sum in a second page. (Ref: home.html and result.html)

13. Use POST function explicitly instead of the deafult GET (In the html form section and in the method in views.py as well)

14. You need to use the CSRF middleware to protect against the CSRF attack. Mention it in {{}} format in the HTML form

15. Make a new static folder where all the necessary files/folders for the html will be kept. Link it through Static in settings.py. Check at the very end.
		
		# This is how the static folder will be referred
		STATIC_URL = '/static/'

		# Telling django where it would find the static files
		STATICFILES_DIRS = [
		    os.path.join(BASE_DIR, 'static')
		]

		# But django will pick up all the static folders and keep them in this particular folder altogether
		# assets can be replaced by any name
		STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

		# But just telling it to create it here won't create the folder automatically. Use the command below after editing here
		# python manage.py collectstatic

		# In the next step all the href in the html must be edited. "{% static " should be added to the begin of each href
		# Ex. href="plugins/default.css" will be changed to href="{static 'plugins/default.css' %}"
		# This makes sense because even after all these, the html will still try to load as it's told in the href
		# You should tell it to find it in the django way
		# Also don't forget to load the static files first at the top of the html by typing
		# {% load static %}

16. Passing informations dynamically:
	Create a class in models.py
	Instantiate them views.py and pass them as a single object
	Acess them like variables, i.e. {{obj.field}}

17. To create superuser
	python manage.py createsuperuser

18. Create an upload page in admin.py automatically by just adding this line (Remember to import the model first)
	admin.site.register(Destination)

19. For handling media files, settings.py needs to be updated and media path needs to be added

20. Once the model is linked with the database it's easy peasy to get them in the views. Just like this:
	Destination.objects.all()


# To get back to a previous environment
	pipenv shell

# To delte an app just remove its name from the INSTALLED_APPS section in project's settings.py file

Credentials:
	User: farhan
	Password: password
