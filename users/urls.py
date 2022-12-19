"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
	# Include default auth urls.
	path('', include('django.contrib.auth.urls')), # http://localhost:8000/users/login/ for example would apply here.. login is available in django urls
	path('register/', views.register, name='register'),
]