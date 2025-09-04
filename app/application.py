from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.home_page import HomePage






class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)