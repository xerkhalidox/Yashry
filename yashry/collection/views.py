from django.shortcuts import render
from collection.models import Product
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def return_category_collection(request, category):
    size = request.GET.get("size", '')
    brand = request.GET.get("brand", '')
    gender = request.GET.get("gender", '')
    products = Product.objects.filter(category=category, size__contains=size,
                                      brand__contains=brand, gender__contains=gender)
    brands = products.values('brand').distinct()
    sizes = products.values('size').distinct()
    colors = products.values('color').distinct()
    context = {'products': products, 'brands': brands,
               'colors': colors, 'sizes': sizes,
               'category': category.capitalize()
               }
    return render(request, "collection/category.html", context=context)


def return_product(request, product):
    products = Product.objects.filter(name=product)
    sizes = products.values('size').distinct()
    colors = products.values('color').distinct()
    context = {'colors': colors, 'sizes': sizes,
               'brand': products[0].brand.capitalize(),
               'name': products[0].name.capitalize(),
               'price': products[0].price,
               'gender': products[0].gender,
               }
    return render(request, "collection/product.html", context=context)


def cart(request):
    if(request.method == "POST"):
        product_name = request.POST["name"]
        if(request.session.session_key):
            for key, value in request.session.items():
                print(key)
        product_info = {
            'name': product_name,
            'size': request.POST["size"],
            'color': request.POST["color"],
            'quantity': request.POST["quantity"],
            'price': request.POST["price"],
            'total': int(request.POST["quantity"])*int(request.POST["price"])
        }
        request.session[product_name] = product_info
        return HttpResponseRedirect(reverse('cart'))
    else:
        return render(request, 'collection/cart.html')


def delete_item_from_cart(request, product_name):
    del request.session[product_name]
    return HttpResponse(status=204)
