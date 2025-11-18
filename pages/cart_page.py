from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_btn = page.get_by_role("button", name="Checkout")

    def proceed_to_checkout(self):
        self.checkout_btn.click()
