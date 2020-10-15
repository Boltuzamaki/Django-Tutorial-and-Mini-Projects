# Django-Tutorial-and-Mini-Projects

## Installation
```sh
pip install django
```
Then open the anaconda terminal and first type
```sh
django-admin startproject firstsite
```
This will automatically create a project named as **firstsite**. Wich create some files automatically which will be used furter.
```sh
django-admin startproject firstsite
```

### **What Is __init__.py?**
- This file is generated by Django for us. It is mandatory to have an __inti__.py file in a directory to denote that the project is a python package and can be imported into other files. This file usually remains empty.
- If this file gets missing, you will see “package not found error” in the absence of this file.
### **What Is settings.py?**
- This is the core file of our Django projects.
- It contains the configuration values which are needed by web apps to work properly such as database settings, static files location, template location, etc. We will keep coming to this file to edit the project configuration throughout this course.
### **What is urls.py?**
- Url declaration and mapping are made under this file.
### **What is wsgi.py?**
- WSGI stands for web-server gateway interface.
- WSGI is a specification that describes the communication between a web server and a web application.
### **What is manage.py?**
- Command-line utility for performing administrative tasks.
- We will be using manage.py frequently while developing a Django project.

In project folder run
```sh
python manage.py runserver
```
To start server . First server is started running successfully :)

### How Websites works
#### **Front-End:**
- It is a combination of HTML, CSS, and Javascript.

- Users can directly view and interact with this data.

- It is also referred to as client-side or frontend design.

#### **Back-end:**
- Back-end takes care of when and which webpage should be visible to the client corresponding to a given request.

- Users can not directly view or interact with this data. The back-end is all about the behind-the-scene activities.

- It is also referred to as the server-side.

## Creating first page and building urls.py

Create a views.py file in project folder which contains urls.py
#### In urls.py
```sh
from . import views
```
```sh
urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('about/', views.about, name='about'), # this is how new path of function in views.py is added to base url
]
```
```sh
from django.http import HttpResponse

def index(request):
    return HttpResponse('''Welcome to first route made in django''')

def about(request):
    return HttpResponse("But wait this is the second one")    # HttpResponse wrap text in html
```    
http://127.0.0.1:8000/about/
This will show you a page which gives an output which present in http response of about.

## Django Templates

#### Updating settings.py file
We have to specify in seerings.py that there is a template folder in which we are putting the templates.Like this
```sh
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]
```
All the html files can go in a newly created folder named templates.To access this we have to make changes in views.py
```sh
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

## Creating an App and Add App.
```sh
python manage.py startapp appname
```
- Create a urls.py inside app to map its views.py things
```sh
from django.conf.urls import url
from . import views

urlpatters = [
url(r'^$', views.description_page),
]
```

- And create views.py inside app
```sh
from django.shortcuts import render

# Create your views here.

def description_page(request):
	return render(request, 'desc_page/description_page.html')
```
- Add that app in settings.py add 'desc_page' like this
```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'desc_page',
]
```
- Now join the urls.py of created app to mainm project urls.py
```sh
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('desc_page.urls')),
]
```
