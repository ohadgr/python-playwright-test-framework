class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.products_title = page.get_by_text("Products", exact=True)
        self.backpack_add_to_cart_button = page.locator('#add-to-cart-sauce-labs-backpack')
        self.cart_added_btn = page.get_by_role("button", name="Cart, 1 items")

    def add_backpack_to_cart(self):
        self.backpack_add_to_cart_button.click()

    def open_cart(self):
        self.cart_added_btn.click()
