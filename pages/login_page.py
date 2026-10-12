class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_text(
            "Epic sadface: Username and password do not match any user in this service",
            exact=True)

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()