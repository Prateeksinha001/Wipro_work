import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.cart_page import CartPage


@pytest.mark.product
def test_product_search(driver, test_data):

    home_page = HomePage(driver)
    search_page = SearchPage(driver)

    product = test_data["product"]

    home_page.search_product(product)

    actual_product = search_page.get_product_name()

    assert product.lower() in actual_product.lower()


@pytest.mark.product
def test_add_product_to_cart(driver, test_data):

    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    cart_page = CartPage(driver)

    product = test_data["product"]

    home_page.search_product(product)

    search_page.select_product()
    search_page.add_to_cart()

    cart_page.open_cart()

    cart_product = cart_page.get_product_name()

    assert product.lower() in cart_product.lower()


@pytest.mark.product
def test_update_cart_quantity(driver, test_data):

    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    cart_page = CartPage(driver)

    product = test_data["product"]

    home_page.search_product(product)
    search_page.select_product()
    search_page.add_to_cart()

    cart_page.open_cart()
    cart_page.update_quantity(2)

    quantity = cart_page.get_quantity()

    assert quantity == "2"