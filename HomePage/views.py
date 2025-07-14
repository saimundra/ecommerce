from django.shortcuts import render
from django.http import HttpResponse
from addproduct.models import product

# Create your views here.
def getproduct(request):
    products = product.objects.all()

    return render(request , "products.html", {"products": products})


