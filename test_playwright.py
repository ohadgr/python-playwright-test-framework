import re
from playwright.sync_api import expect
from pages.login_page import LoginPage

# def test_open_page(page):
#     page.goto("https://playwright.dev")
#     heading = page.get_by_role("heading", level=1)
#     expect(heading).to_be_visible()
#     expect(heading).to_contain_text("Playwright")
#
#     get_started = page.get_by_role("link", name="Get started")
#     get_started.click()
#     expect(page).to_have_url(re.compile(r".*/docs/intro"))
#     installation_header = page.get_by_role("heading", level=1, name="Installation")
#     expect(installation_header).to_be_visible()
#
#
# def test_docs_navigation(page):
#     page.goto("https://playwright.dev")
#     get_started_link = page.get_by_role("link", name="Get Started")
#     expect(get_started_link).to_be_visible()
#     get_started_link.click()
#     expect(page).to_have_url(re.compile(r".*/docs/intro"))
#     installation_header = page.get_by_role("heading", name="Installation")
#     expect(installation_header).to_be_visible()





