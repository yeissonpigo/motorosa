from django.http import HttpResponse
from django.shortcuts import render
from .models import TypeProduct

# Create your views here.

def insertTypeProduct(request):
    typeProduct = TypeProduct.objects.create(
        name = 'accesory',
        desc = 'This is something you put on your vehicle'
    )
    
    typeProduct.save()
    return HttpResponse('Test')

def showTypeProducts(request):
    products = TypeProduct.objects.all()
    myproducts = []
    for x in products:
        myproducts.append(x.name)
    return HttpResponse(myproducts)