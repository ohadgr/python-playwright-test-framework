import re

from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.products_page import ProductsPage


def test_add_backpack_to_cart(logged_in_page):
    products_page = ProductsPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    products_page.add_backpack_to_cart()
    expect(products_page.cart_added_btn).to_contain_text("1")
    products_page.open_cart()
    expect(logged_in_page).to_have_url(re.compile(r".*/cart.html"))
    expect(cart_page.backpack_item).to_be_visible()
