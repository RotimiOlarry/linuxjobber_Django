import os 
from setuptools import find_packages, setup 

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
	name = 'django-timiolarryscrumy',
	version = '0.1',
	packages = find_packages(),
	include_package_data = True,
	license = 'BSD license ', #example
	description = 'A simple django web-based to-do app',
	long_description = 'README',
	url = 'http:/3.2.4.14:8000/timiolarryscrumy/',
	author = 'Rotimi Olarewaju',
	author_email = 'timiolarry@gmail.com',
	classifiers = [
		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django 3.0.6',
		'License :: OSI Approved :: BSD license', #Example
		'Operating system :: OS Independent',
		'Programming language :: Python',
		'Programming language :: Python 3.7.3',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		
	],
)

