# Code taken from django projects intro tutorial

from django.urls import path

from . import views

urlpatterns = [
    path('<key>', views.key, name='key'),
]
