from django.shortcuts import render,redirect
from django.http import HttpResponse 
from addproduct.models import product

# Create your views here.
def addproduct(request):
    if request.method == "GET":
        products = product.objects.all()
        return render(request,'addproduct.html',{'products': products})
    elif request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        description = request.POST["description"]
        image = request.FILES.get("image")
        newproduct = product(name=name, description=description, price=price, image=image)
        newproduct.save()
        return redirect('/')
    else:
        return HttpResponse("invalid credentials")
    

def updateProduct(request, product_id):
    if request.method == "POST":
        productTobeUpdated = product.objects.get(id=product_id)
        productTobeUpdated.name = request.POST['productName']
        productTobeUpdated.price = request.POST['price']
        productTobeUpdated.description = request.POST['description']
        if 'image' in request.FILES:
            productTobeUpdated.image = request.FILES['image']
        productTobeUpdated.save()
        return HttpResponse('Product updated successfully')
    else:
        return HttpResponse('Invalid Request Method')

def deleteProduct(request, product_id):
    if request.method == "POST":
        try:
            productTobeDeleted = product.objects.get(id=product_id)
            productTobeDeleted.delete()
            return HttpResponse('Product deleted successfully')
        except product.DoesNotExist:
            return HttpResponse('Product not found', status=404)
    else:
        return HttpResponse('Invalid Request Method', status=405)




