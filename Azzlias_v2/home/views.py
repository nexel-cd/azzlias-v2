from django.shortcuts import render
from .models import *
# Create your views here.



def home(request):
    categories = Category.objects.all()
    bestseller = BestSeller.objects.all()
    content = {
       "categories":categories ,
       "bestseller":bestseller
    }
    return render(request, 'index.html',content)


def category(request):
    categories = Category.objects.all()
    content = {
       "categories":categories 
    }
    return render(request, 'category.html',content)


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop.html', context)

def shop_details(request,pk):
    products_data = Product.objects.filter(slug=pk)
    products_data_inst = Product.objects.get(slug=pk)
    images = ProductImage.objects.filter(product=products_data_inst)
    categories = Category.objects.all()

    context = {
        'products_data': products_data,
        'categories': categories,
        "images":images
    }
    return render(request, 'product_details.html', context)

def shop_category(request,cat):
    categories = Category.objects.get(slug=cat)
    products_data = Product.objects.filter(category=categories)
    

    context = {
        'products': products_data,
        'categories': categories,
        
    }
    return render(request, 'shop.html', context)


def contactus(request):
    return render(request,'contact.html')