class CheckoutInformationPage:
    def __init__(self, page):
        self.page = page
        self.first_name_field = page.get_by_placeholder("First Name")
        self.last_name_field = page.get_by_placeholder("Last Name")
        self.zip_code_field = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="continue")
        self.cancel_button = page.get_by_role("button", name="cancel")
        self.first_name_error_message = page.get_by_text(
            "Error: First Name is required",
            exact=True)
        self.last_name_error_message = page.get_by_text(
            "Error: Last Name is required",
            exact=True)
        self.postal_code_error_message = page.get_by_text(
            "Error: Postal Code is required",
            exact=True)
        self.error_message = page.locator('[data-test="error"]')

    def fill_information(self,
                         first_name,
                         last_name,
                         zip_code
                         ):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.zip_code_field.fill(zip_code)

    def continue_checkout(self):
        self.continue_button.click()


