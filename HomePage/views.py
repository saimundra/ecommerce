from django.shortcuts import render
from django.http import HttpResponse
from addproduct.models import product

# Create your views here.
def getproduct(request):
    products = product.objects.all()
    for product1 in products.values():
        print(product1['name'])
    return render(request , "products.html", {"products": products})
