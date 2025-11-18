from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.zip_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_btn = page.get_by_role("button", name="Continue")
        self.finish_btn = page.get_by_role("button", name="Finish")

    def fill_checkout_info(self, fname, lname, zip):
        self.first_name.fill(fname)
        self.last_name.fill(lname)
        self.zip_code.fill(zip)

    def continue_checkout(self):
        self.continue_btn.click()

    def finish_order(self):
        self.finish_btn.click()
