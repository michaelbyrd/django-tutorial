

# Run the server
- python manage.py runserver

# Dependencies
- pip install -r requirments.txt --> This will install the dependencies
- pip freeze > requirements.txt --> This will update requirments.txt with your current virtualenv's libraries

# Notes

## Generic views
- in /polls/views.py --> from django.views import generic
- DetailView template --> \<app name\>/\<model name\>_detail.html
- ListView template --> \<app name\>/\<model name\>_list.html

# Testing
- python manage.py test \<app name\> <-- run the test found in the \<app name\>
- response.context(\<context object name\>) will return the objects used to
  render the view
- response.content will return the html (or json etc)

# Packaging the Polls app
- move the polls directory into a django-polls directory ousite of mysite
- create a file django-polls/README.rst
- create django-polls/setup.py
- create django-polls/MANIFEST.in <-- has recursive-include config commands
- cd into django-polls and run: python setup.py sdist <-- this builds the
  package
- pip install --user django-polls/dist/django-polls-0.1.tar.gz (remove --user to
  work with virtualenvwrapper

# Resources
- [VirtualEnv][]
- [Django Tutorial][]


[virtualenv]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
[django tutorial]: https://docs.djangoproject.com/en/1.8/intro/tutorial01/
