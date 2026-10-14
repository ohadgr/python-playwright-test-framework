class CartPage:
    def __init__(self, page):
        self.page = page
        self.backpack_item = page.get_by_text("Sauce Labs Backpack", exact=True)
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.remove_backpack_button = page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.cart_button = page.locator('#shopping-cart-link')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.continue_shopping_button = page.get_by_role("button", name="Continue Shopping")
        self.bike_light_item = page.get_by_text("Sauce Labs Bike Light", exact=True)

    def click_on_checkout_button(self):
        self.checkout_button.click()

    def click_on_remove_backpack_button(self):
        self.remove_backpack_button.click()

    def click_on_continue_shopping_button(self):
        self.continue_shopping_button.click()