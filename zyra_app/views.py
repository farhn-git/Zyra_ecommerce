from django.shortcuts import redirect, render
from zyra_app.models import *


# user panel

def viewhome(request):
    res=Collection.objects.all()
    return render(request,'users/index.html',{'data':res})

def view_product(request):
    res=Collection.objects.all()
    res1=Products.objects.all()
    return render(request,'users/products.html',{'data1':res1,'data':res})




# ADMIN PANEL 

def adminhome(request):
    return render(request, 'admin/index.html')

def viewproducts(request):
    res=Products.objects.all()
    return render(request,'admin/products.html',{'data':res})


def addproducts(request):
    res=Collection.objects.all()
    return render(request,'admin/addproduct.html',{'data':res})

def addproducts_post(request):
    if request.method == "POST":
        n = request.POST.get("name")
        p = request.POST.get("price")
        q = request.POST.get("quantity")
        i1 = request.FILES.get("image1")
        i2 = request.FILES.get("image2")
        c_id = request.POST.get("collection")

        collection = Collection.objects.get(id=c_id)

        products = Products(
            name=n,
            price=p,
            quantity=q,
            image1=i1,
            image2=i2,
            COLLECTION=collection,
        )
        products.save()
        return redirect('viewproducts')
    
def addcollection(request):
    res=Collection.objects.all()
    return render(request,'admin/collection.html',{'data':res})

def addcollection_post(request):
    if request.method == "POST":
        n = request.POST.get("name")

        collection = Collection(
            name=n,
        )
        collection.save()
        return redirect('addcollection')




def viewdashbaord(request):
    return render(request,'admin/dashboard.html')

def vieworder(request):
    return render(request,'admin/orders.html')

def viewpayments(request):
    return render(request,'admin/payments.html')

def viewcustomers(request):
    return render(request,'admin/customers.html')