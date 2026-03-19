import requests

BASE_URL = "https://dummyjson.com"
PRODUCTS_PATH = "/products"
PRODUCT_BY_ID_PATH = "/products/{id}"
PRODUCTS_SEARCH_PATH = "/products/search"


def get_all_products(token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.get(BASE_URL + PRODUCTS_PATH, headers=headers)


def get_product_by_id(token, product_id):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.get(BASE_URL + PRODUCT_BY_ID_PATH.format(id=product_id), headers=headers)


def search_products(token, query):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.get(BASE_URL + PRODUCTS_SEARCH_PATH, params={"q": query}, headers=headers)
