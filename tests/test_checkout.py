import re

import pytest
from playwright.sync_api import expect

from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.price_utils import parse_price


def test_backpack_checkout(logged_in_page):
    products_page = ProductsPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_information_page = CheckoutInformationPage(logged_in_page)
    checkout_overview_page = CheckoutOverviewPage(logged_in_page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page.click_on_checkout_button()
    expect(logged_in_page).to_have_url(re.compile(r".*/checkout-step-one.html"))
    checkout_information_page.fill_information("test", "user", "90210")
    checkout_information_page.continue_checkout()
    expect(logged_in_page).to_have_url(re.compile(r".*/checkout-step-two.html"))
    expect(checkout_overview_page.backpack_item).to_be_visible()
    expect(checkout_overview_page.quantity_backpack).to_have_text("1")
    expect(checkout_overview_page.payment_info_value).to_contain_text(
        "SauceCard #31337"
    )
    item_price = parse_price(checkout_overview_page.item_price.inner_text())
    item_total = parse_price(checkout_overview_page.item_total_price.inner_text())
    tax = parse_price(checkout_overview_page.tax.inner_text())
    total = parse_price(checkout_overview_page.total_price.inner_text())
    assert item_price == item_total
    assert item_total + tax == total


@pytest.mark.parametrize(
    "first_name, last_name, zip_code, expected",
    [
        ("", "User", "90210", "Error: First Name is required"),
        ("Test", "", "90210", "Error: Last Name is required"),
        ("Test", "User", "", "Error: Postal Code is required"),
    ]
)
def test_negative_validation(logged_in_page, first_name, last_name, zip_code, expected):
    products_page = ProductsPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_information_page = CheckoutInformationPage(logged_in_page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page.click_on_checkout_button()
    checkout_information_page.fill_information(first_name, last_name, zip_code)
    checkout_information_page.continue_checkout()
    expect(checkout_information_page.error_message).to_have_text(expected)
