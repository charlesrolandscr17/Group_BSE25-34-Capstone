from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Product

# Create your views here


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product_detail.html', {'product': product})
