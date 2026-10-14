class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.products_title = page.get_by_text("Products", exact=True)
        self.backpack_add_to_cart_button = page.locator('#add-to-cart-sauce-labs-backpack')
        self.bike_light_add_to_cart_button = page.locator('#add-to-cart-sauce-labs-bike-light')
        self.shopping_cart_button = page.locator('[data-test="shopping-cart-link"]')

    def add_backpack_to_cart(self):
        self.backpack_add_to_cart_button.click()

    def add_bike_light_to_cart(self):
        self.bike_light_add_to_cart_button.click()

    def open_cart(self):
        self.shopping_cart_button.click()
