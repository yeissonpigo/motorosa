from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import TypeProduct
from .forms import inputTypeProduct

# Create your views here.

def insertTypeProduct(request):
    if request.method == 'GET':
        form = inputTypeProduct()
        return render(request, 'store/createProduct.html', {'form': form})
    elif request.method == 'POST':
        myTypeProduct = inputTypeProduct(request.POST)
        if myTypeProduct.is_valid():
            myTypeProduct.save()
        return redirect('insert_type_product')
    return HttpResponse('Test')

def getTypeProduct(request):
    if request.method == 'GET':
        return render(request, 'store/searchProduct.html')
    if request.method == 'POST':
        myId = request.POST['productId']
        myTypeProduct = TypeProduct.objects.get(id = myId)
        return render(request, 'store/showProduct.html', {'products': myTypeProduct})

def showTypeProducts(request):
    products = TypeProduct.objects.all()
    myproducts = []
    for x in products:
        myproducts.append(x.name)
    return HttpResponse(myproducts)