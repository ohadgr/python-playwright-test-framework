import re

from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.products_page import ProductsPage


def test_add_backpack_to_cart(logged_in_page):
    products_page = ProductsPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    products_page.add_backpack_to_cart()
    expect(products_page.shopping_cart_button).to_contain_text("1")
    products_page.open_cart()
    expect(logged_in_page).to_have_url(re.compile(r".*/cart.html"))
    expect(cart_page.backpack_item).to_be_visible()

def test_remove_backpack_from_cart(logged_in_page):
    products_page = ProductsPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    expect(logged_in_page).to_have_url(re.compile(r".*/cart.html"))
    expect(cart_page.backpack_item).to_be_visible()
    expect(cart_page.cart_badge).to_contain_text("1")
    cart_page.click_on_remove_backpack_button()
    expect(cart_page.backpack_item).not_to_be_visible()
    expect(cart_page.cart_badge).not_to_be_visible()

def test_add_second_item_to_cart(logged_in_page):
    products_page = ProductsPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    expect(cart_page.backpack_item).to_be_visible()
    expect(cart_page.cart_badge).to_contain_text("1")
    cart_page.click_on_continue_shopping_button()
    expect(logged_in_page).to_have_url(re.compile(r".*/inventory.html"))
    products_page.add_bike_light_to_cart()
    expect(products_page.shopping_cart_button).to_contain_text("2")
    products_page.open_cart()
    expect(cart_page.backpack_item).to_be_visible()
    expect(cart_page.bike_light_item).to_be_visible()
    expect(cart_page.cart_badge).to_contain_text("2")




