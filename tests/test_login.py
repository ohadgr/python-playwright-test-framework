import re

from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_login(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url(re.compile(r".*/inventory.html"))
    expect(products_page.products_title).to_be_visible()


def test_login_with_wrong_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")
    expect(login_page.error_message).to_be_visible()
