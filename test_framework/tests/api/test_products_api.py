import pytest
from pages.api.products_api import get_all_products, get_product_by_id, search_products  # ← fixed
from conftest import auth_token
def test_get_all_products(auth_token):
    response = get_all_products(auth_token)
    print("All Products:", response.text)
    assert response.status_code == 200
    assert "products" in response.json()

def test_get_product_by_id(auth_token):
    response = get_product_by_id(auth_token, 1)
    print("Product by ID:", response.text)
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_search_products(auth_token):
    response = search_products(auth_token, "phone")
    print("Search Products:", response.text)
    assert response.status_code == 200
    assert "products" in response.json()