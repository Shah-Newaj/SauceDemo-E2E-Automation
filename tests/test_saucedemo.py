from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_saucedemo(page):
    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Login Page
    login.load()
    login.login("standard_user", "secret_sauce")

    # Products Page
    products.add_backpack_to_cart()
    products.open_cart()

    # Cart Page
    cart.proceed_to_checkout()

    # Checkout Page
    checkout.fill_checkout_info("Shah", "Newaj", "6000")
    checkout.continue_checkout()
    checkout.finish_order()
