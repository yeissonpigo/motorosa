from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('inserttype', views.insertTypeProduct, name='insert_type_product'),
    path('show', views.showTypeProducts, name='show'),
]