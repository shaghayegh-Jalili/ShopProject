from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


def index(request):
    # return render(request,'index.html')
    return redirect(reverse("shop:store"))


def store(request):
    return render(request,'store.html')


def checkout(request):
    return render(request,'checkout.html')


def product(request):
    return render(request,'product.html')
