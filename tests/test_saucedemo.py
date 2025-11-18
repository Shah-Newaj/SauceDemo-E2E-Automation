from playwright.sync_api import expect

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
    # Assert login success (URL should contain /inventory)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("✅ URL matched successfully!")

    # Products Page
    products.add_backpack_to_cart()
    products.open_cart()
    # Assert cart page title
    expect(page).to_have_title("Swag Labs")
    print("✅ Cart Page Title matched successfully!")

    # Cart Page
    cart.proceed_to_checkout()
    # Assert we are on checkout step one page
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    print("✅ checkout step one page matched successfully!")

    # Checkout Page
    checkout.fill_checkout_info("Shah", "Newaj", "6000")
    checkout.continue_checkout()
    checkout.finish_order()
    # Assert success message appears
    success_msg = page.locator(".complete-header")
    expect(success_msg).to_have_text("Thank you for your order!")
    print("✅ Success message is shown after finishing the order")
