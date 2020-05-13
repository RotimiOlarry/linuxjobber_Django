=================
Timiolarryscrumy
=================

Timiolarrycrummy is a basic to-do application that helps us manage our daily to do task and assign task to others from the application.

Detailed documentation is in the "docs" directory.

Quick Start
-----------
1. Add "timiolarryscrummy" to your INSTALLED APPS setting like this::

	INSTALLED_APPS = [
	......
	'timiolarryscrumy',
	]

2. Include timiolarryscrumy URLconf in the urls.py like this ::

	path('timiolarryscrumy/', include ('timiolarryscrumy')),

3. Run 'python manage.py migrate' to create models.

4. Start the development server and visit http:/127.0.0.1:8000/admin/ to 	create 
	a a todo (You'll need the Admin app enabled).

5. Visit http:/127.0.0.1:8000/timiolarryscrumy/ to seee the to-do tasks 


