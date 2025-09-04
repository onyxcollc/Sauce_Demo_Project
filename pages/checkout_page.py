from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage




class CheckoutPage(BasePage):

    FIRST_NAME = (By.CSS_SELECTOR,"[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR,"[data-test='lastName']")
    ZIP_CODE = (By.CSS_SELECTOR,"[data-test='postalCode']")
    CONTINUE_BTN = (By.CSS_SELECTOR,"[data-test= 'continue']")
    FINISH_BTN = (By.CSS_SELECTOR,"[data-test= 'finish']")
    CHECKOUT_COMPLETE = (By.XPATH,"//span[text()='Checkout: Complete!']")




    def checkout_info(self):
        self.input_text('Luke',*self.FIRST_NAME)
        sleep(1)
        self.input_text('Davis',*self.LAST_NAME)
        sleep(1)
        self.input_text('85029',*self.ZIP_CODE)
        sleep(1)


    def continue_btn(self):
        self.click(*self.CONTINUE_BTN)



    def finish_btn(self):
        sleep(2)
        self.click(*self.FINISH_BTN)


    def verify_checkout_complete(self):
        expected = "Checkout: Complete!"
        actual = self.driver.find_element(*self.CHECKOUT_COMPLETE)
        assert expected == actual.text,f"Expected {expected} but got {actual.text}"
        sleep(3)