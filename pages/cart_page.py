class CartPage:
    def __init__(self, page):
        self.page = page
        self.backpack_item = page.get_by_text("Sauce Labs Backpack", exact=True)
