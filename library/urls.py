from django.urls import path
from .           import views

urlpatterns = [
    path('', views.init, name='init'),
    path('contact', views.contact, name='contact'),
]