from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def products(request):

    """
    Displays all products and handles search queries
    """

    products = Product.objects.all()
    search_query = None

    if request.GET:
        if 'query' in request.GET:
            search_query = request.GET['query']
            if not search_query:
                messages.error(request, 'Oops! Search box was empty.')
                return redirect(reverse('products'))

            search_q = Q(description__icontains=search_query) | Q(name__icontains=search_query)
            products = products.filter(search_q)

        

    context = {
        'products': products,
        'searched_item': search_query,
    }

    return render(request, 'products/products.html', context)
