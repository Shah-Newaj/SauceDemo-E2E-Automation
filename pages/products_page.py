from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_backpack_btn = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_backpack_to_cart(self):
        self.add_backpack_btn.click()

    def open_cart(self):
        self.cart_icon.click()
