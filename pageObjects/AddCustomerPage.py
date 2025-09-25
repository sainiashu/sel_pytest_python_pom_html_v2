import time
from asyncio import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import select

class AddCustomer:
    lnkCustomerMenu = "/html[1]/body[1]/div[3]/aside[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    lnkCustomerMenuItems ="/html[1]/body[1]/div[3]/aside[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btn_AddNew = "//a[@class='btn btn-primary']"
    txtEmail = "Email"
    txtPassword = "Password"

    txtFirstName = "FirstName"
    txtLastName = "LastName"
    txtCustomerRole = "/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]/ul[1]"
    btn_Save = "//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomerMenu).click()

    def clickOnCustomerMenuItems(self):
        self.driver.find_element(By.XPATH, self.lnkCustomerMenuItems).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.ID, self.btn_AddNew).click()

    def enterEmail(self, email):
        self.driver.find_element(By.ID,self.txtEmail).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.ID,self.txtPassword).send_keys(password)

    def enterFirstName(self, firstName):
        self.driver.find_element(By.ID,self.txtFirstName).send_keys(firstName)

    def enterLastName(self, lastName):
        self.driver.find_element(By.ID,self.txtLastName).send_keys(lastName)

    def enterCustomerRole(self, customerRole):
        self.driver.find_element(By.XPATH,self.txtCustomerRole).send_keys(customerRole)

    def clickOnSave(self):
        self.driver.find_element(By.ID,self.btn_Save).click()

