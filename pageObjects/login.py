from selenium import  webdriver
from  selenium.webdriver.common.by import By


class LoginPage:
    textbox_username = "Email"
    textbox_password = "Password"
    btn_login = "//button[@type='submit']"
    btn_logout = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username).clear()
        self.driver.find_element(By.ID, self.textbox_username).send_keys(username)

    def enter_password(self, password):
            self.driver.find_element(By.ID, self.textbox_password).clear()
            self.driver.find_element(By.ID, self.textbox_password).send_keys(password)

    def click_login(self):
            self.driver.find_element(By.XPATH, self.btn_login).click()

    def click_logout(self):
            self.driver.find_element(By.XPATH, self.btn_logout).click()
