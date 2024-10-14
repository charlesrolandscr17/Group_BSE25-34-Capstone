from django.shortcuts import get_object_or_404, render, HttpResponse
from django.views import View
from .models import Product
from price_aggregator.helpers.scraper import amazon_list
# Create your views here


# class ProductListView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'product_list.html', {'scraped_data': []})

#     def post(self, request, *args, **kwargs):
#         query = request.POST.get('query')  # Retrieve the search details
#         if query:
#             products = amazon_list(query)
#             return render(
#                 request, 'product_list.html', {
#                     'scraped_data': products})
#         return render(request, 'product_list.html', {'scraped_data': []})


def product_list(request):
    try:
        query = request.GET["query"]  # Retrieve the search details
        print(query)
    except:
        return HttpResponse("Error Occured")
    if query:
        products = amazon_list(query)
        print(products)
        return render(
            request, 'product_list.html', {
                'scraped_data': products})
    return render(request, "product_list.html", {"scraped_data": []})


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, "product_detail.html", {"product": product})
