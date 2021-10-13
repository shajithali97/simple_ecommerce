from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product 
# Q for Query
from django.db.models import Q
# Create your views here.
def search_result(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(product_name__contains=query) | Q(description__contains=query))
        context={
            'query':query,
            'products':products
        }
        return render(request,'search.html',context)
