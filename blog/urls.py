#Here we are importing from Django every function url and all views from blog

from django.urls import path
from . import views

#Adding our first pattern from URLs
#We are attibuting a view called post_list to URL root
#views.post_list is the right place to go if someone access the following path: http://127.0.0.1:8000
urlpatterns = [
    path('', views.post_list, name = 'post_list'),
]
#name = 'post_list' é o nome da URL
