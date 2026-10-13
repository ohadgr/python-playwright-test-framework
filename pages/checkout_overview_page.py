class CheckoutOverviewPage:
    def __init__(self, page):
        self.page = page
        self.backpack_item = page.get_by_text("Sauce Labs Backpack", exact=True)
        self.finish_button = page.get_by_role("button", name="Finish")
        self.cancel_button = page.get_by_role("button", name="cancel")
        self.item_price = page.locator('[data-test="inventory-item-price"]')
        self.item_total_price = page.locator('[data-test="subtotal-label"]')
        self.tax = page.locator('[data-test="tax-label"]')
        self.total_price = page.locator('[data-test="total-label"]')
        self.quantity_backpack = page.locator('[data-test="item-quantity"]')
        self.payment_info_value = page.locator('[data-test="payment-info-value"]')

    def click_on_finish_checkout(self):
        self.finish_button.click()
