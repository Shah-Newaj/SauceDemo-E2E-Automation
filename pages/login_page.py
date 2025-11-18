from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.locator("#password")
        self.login_btn = page.get_by_role("button", name="Login")

    def load(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
