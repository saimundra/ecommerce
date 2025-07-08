from  django.urls import path
from . import views
urlpatterns =[
    path("",views.addproduct , name= "addproduct"),
    path('updateProduct/<uuid:product_id>', views.updateProduct),
    path('deleteProduct/<uuid:product_id>', views.deleteProduct)
] 