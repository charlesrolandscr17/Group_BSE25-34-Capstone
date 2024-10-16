import requests


def amazon_list(search):
    url = "https://amazon-merchant-data.p.rapidapi.com/search-products"

    querystring = {"term": search, "country": "us"}

    headers = {
        "x-rapidapi-key": "1f80a503a5mshfe1fc74c6f7d90ep13625djsn7aff620569dd",
        "x-rapidapi-host": "amazon-merchant-data.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


# amazon_list("Samsung galaxy S23")


def ebay_list(search):
    url = "https://ebay-average-selling-price.p.rapidapi.com/findCompletedItems"

    payload = {
        "keywords": search,
        "excluded_keywords": "locked cracked case box read LCD",
        "max_search_results": "60",
        "remove_outliers": "true",
        "aspects": [
            {"name": "Model", "value": search},
        ],
    }
    headers = {
        "x-rapidapi-key": "1f80a503a5mshfe1fc74c6f7d90ep13625djsn7aff620569dd",
        "x-rapidapi-host": "ebay-average-selling-price.p.rapidapi.com",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()


# ebay_list("Samsung galaxy S23")
