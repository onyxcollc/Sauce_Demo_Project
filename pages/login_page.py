from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import BasePage
from time import sleep

class LoginPage(BasePage):


    USERNAME = (By.CSS_SELECTOR,"[data-test='username']")
    PASSWORD = (By.CSS_SELECTOR,"[data-test='password']")
    LOGIN_BTN = (By.CSS_SELECTOR,"[data-test='login-button']")
    ERROR_MSG = (By.XPATH,"//*[text()='Epic sadface: Username and password do not match any user in this service']")

    def login_page(self):
        self.open_url()



    def user_name(self,name):
        self.input_text(name,*self.USERNAME)
        sleep(1)


    def password_text(self,password):
        self.input_text(password,*self.PASSWORD)
        sleep(1)


    def login_btn(self):
        self.click(*self.LOGIN_BTN)


    def error_message(self):
        self.verify_text(*self.ERROR_MSG)
