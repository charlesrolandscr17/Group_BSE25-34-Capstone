from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Product

# myapp/views.py
import logging
from django.shortcuts import render

# Configure the logger
logger = logging.getLogger('price_aggregator') 

def your_view(request):
    # Log messages at different levels
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    
    # Your view logic here
    return render(request, 'product_detail.html', {})



class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product_detail.html', {'product': product})
