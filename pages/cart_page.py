from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage



class CartPage(BasePage):


    CART_BTN = (By.CSS_SELECTOR, "[data-test='checkout']")


    def checkout_btn(self):
        self.click(*self.CART_BTN)
        sleep(2)