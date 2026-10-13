class CartPage:
    def __init__(self, page):
        self.page = page
        self.backpack_item = page.get_by_text("Sauce Labs Backpack", exact=True)
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def click_on_checkout_button(self):
        self.checkout_button.click()
