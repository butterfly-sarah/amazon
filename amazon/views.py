from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from amazon.models import product,catagory
# Create your views here.


def home(request):
    products = product.objects.all()
    d = {"products": products}
    return render(request,"amazon/home.html",d)
def contact(request):
    return render(request,"amazon/contact.html")
def about(request):
    return render(request,"amazon/about us.html")
def base(request):
    return render(request,"amazon/layouts/base.html")
def info(request,pro_info):
    item = get_object_or_404(product,pk=pro_info)
    context = {"product": item}
    return render(request,"amazon/info.html",context)
def search(request):
    if request.method=="POST":
        searchname=request.POST["searchname"]
        products=product.objects.filter(product__startswith=searchname)
        context={"product":products}
        return render(request,"amazon/search.html",context)

    elif request.method=="GET":
           return render(request,"amazon/search.html")
def add(request):
    if request.method == "GET":
         p = catagory.objects.all()
         context = {"catagory": p}
         return render(request, "amazon/add.html", context)
    if request.method=="POST":
        pr=product()
        pr.product=request.POST["product"]
        pr.img = request.POST["img"]
        pr.disc = request.POST["disc"]
        pr.price = request.POST["price"]
        m=catagory.objects.get(pk=request.POST["catagory"])
        pr.branch =m
        pr.save()
        return redirect("home")
def delete(request,pro_id):
    products=get_object_or_404(product,pk=pro_id)
    products.delete()
    return redirect("home")
def edit(request,pro_id):
    pass