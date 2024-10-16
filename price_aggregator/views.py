from django.shortcuts import render
from price_aggregator.helpers.scraper import amazon_list
import requests, bs4
# Create your views here


def product_list(request):
    print(request.GET)
    if bool(request.GET):
        query = request.GET["search"]  # Retrieve the search details
        products_1 = amazon_list(query)
        # products_2 = ebay_list(query)
        # print(products_2)

        # print(products_2["products"][0])
        # print(products_1["content"]["offers"][5])

        products = []

        for product in products_1["content"]["offers"]:
            try:
                response = requests.get(product["link"])

                soup = bs4.BeautifulSoup(response.text, "html.parser")

                img = soup.find("img", id="landingImage").get("src")

                products.append(
                    {
                        "title": product["name"],
                        "price": product["price"],
                        "url": product["link"],
                        "img": img,
                        "source": "Amazon",
                    }
                )
                print("done")
            except Exception as e:
                print(f"Error: {e}")

            if len(products) >= 4:
                break

        # print("ebay")
        # for product in products_2["products"]:
        #     print("start")
        #     try:
        #         products.append(
        #             {
        #                 "title": product["name"],
        #                 "price": product["sale_price"],
        #                 "url": product["link"],
        #                 "img": product["image_url"],
        #                 "source": "Ebay",
        #             }
        #         )
        #     except Exception as e:
        #         print(f"Error: {e}")

        #     if len(products) >= 8:
        #         break

        return render(request, "product_list.html", {"products": products})
    return render(request, "product_list.html", {"products": []})
