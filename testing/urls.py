# maps requests to view function
# Imports path function from urls
# imports views from . current directory

from django.urls import path
from . import views

# var to map requests using path function from django.urls
# URLconf module, url configuration.

urlpatterns = [
    path('hello/', views.say_hello),
]