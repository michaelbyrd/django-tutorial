

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

# Resources
- [VirtualEnv][]
- [Django Tutorial][]

[:virtualenv] https://docs.djangoproject.com/en/1.8/intro/tutorial01/
[:django tutorrial] http://docs.python-guide.org/en/latest/dev/virtualenvs/
