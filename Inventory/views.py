from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import *




def index(request):
    return render(request,'index.html')


def display_laptop(request):

    items=Laptop.objects.all()

    return render(request,'index.html',{"items":items,"header":"Laptops"})
def display_desktops(request):

    items=Desktop.objects.all()

    return render(request,'index.html',{"items":items,"header":"Desktops"})
def display_mobiles(request):

    items=Mobiles.objects.all()


    return render(request,'index.html',{"items":items,"header":"Mobiles"})

def add_Devices(request,cls):
    if request.method=="POST":
        form=cls(request.POST)


        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=cls()
        return render(request,'add_new.html',{"form":form})

def add_Laptops(request):

    return add_Devices(request,LaptopsForms,)

def add_Desktop(request):

    return add_Devices(request,DesktopForm)

def add_Mobiles(request):

    return add_Devices(request,MobilesForm)

def edit_device(request,pk,model,cls):
    item=get_object_or_404(model,pk=pk)

    if request.method=="POST":
        form=cls(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=cls(instance=item)

        return render(request,'edit_items.html',{"form":form})

def edit_laptops(request,pk):
    return edit_device(request,pk,Laptop,LaptopsForms)

def edit_desktops(request,pk):
    return edit_device(request,pk,Desktop,DesktopForm)

def edit_mobiles(request,pk):
    return edit_device(request,pk,Mobiles,MobilesForm)