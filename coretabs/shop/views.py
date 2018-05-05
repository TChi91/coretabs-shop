from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category


def product_list(request, slug=None):
    category = None
    products = Product.objects.all()
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products.filter(category=category)
    return render(request, 'shop/all.html',{'products': products, 'categories' : categories, 'category':category})


def product_list2(request, slug=None):
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = category.products.all()
        context = {'category':category, 'products' : products}
    else:
        products = Product.objects.all()
        categories = Category.objects.all()
        context = {'products': products, 'categories' : categories}
    return render(request, 'shop/all.html',context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/details.html', {'product': product})


#def product_list_by_category(request, slug):
 #   category = get_object_or_404(Category, slug=slug)
  #  return render(request, 'shop/list_by_category.html', {'category': category})