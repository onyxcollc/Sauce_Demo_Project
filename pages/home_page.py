from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep


from pages.base_page import BasePage


class HomePage(BasePage):

    SWAG_LABS = (By.XPATH,"//div[text()='Swag Labs']")
    BACK_PACK = (By.CSS_SELECTOR,"[data-test='add-to-cart-sauce-labs-backpack']")
    BIKE_LIGHT = (By.CSS_SELECTOR,"[data-test='add-to-cart-sauce-labs-bike-light']")
    T_SHIRT = (By.CSS_SELECTOR,"[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
    FLEECE_JACKET = (By.CSS_SELECTOR,"[data-test='add-to-cart-sauce-labs-fleece-jacket']")
    CART_BADGE = (By.CSS_SELECTOR,"[data-test='shopping-cart-badge']")
    CART_ICON = (By.CSS_SELECTOR,"[data-test='shopping-cart-link']")




    def verify_user_logged_in(self):
        self.verify_partial_url("inventory.html")
        sleep(5)

    def add_items_to_cart(self):
        self.click(*self.BACK_PACK)
        sleep(1)
        self.click(*self.BIKE_LIGHT)
        sleep(1)
        self.click(*self.T_SHIRT)
        sleep(1)
        self.click(*self.FLEECE_JACKET)
        sleep(1)

    def cart_badge_number_updates(self,expected_count: int):
        actual_el = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.CART_BADGE)
        )
        actual = int(actual_el.text.strip())
        assert actual == expected_count, f"Expected {expected_count} got {actual}"

        # expected = '4'
        # actual = self.find_element(*self.CART_BADGE)
        # assert expected in actual.text,f"{expected}is not in {actual.text}"

    def click_cart_icon(self):
        self.click(*self.CART_ICON)
        sleep(2)