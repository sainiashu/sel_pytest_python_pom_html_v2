from selenium.webdriver.common.by import By

class AddCustomerRoles:
    lnkCustomerMenu = (By.XPATH, "/html[1]/body[1]/div[3]/aside[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]")
    lnkCustomerRoles = (By.XPATH, "//p[normalize-space()='Customer roles']")
    btnAddNew = (By.XPATH, "//i[@class='fas fa-square-plus']")
    # txtName = "Name"
    txtName = (By.ID,"Name")
    btnSave = (By.XPATH, "//button[@name='save']//i[@class='far fa-floppy-disk']")

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(*self.lnkCustomerMenu).click()

    def clickOnCustomerRoles(self):
        self.driver.find_element(*self.lnkCustomerRoles).click()

    def clickOnAddNew(self):
        self.driver.find_element(*self.btnAddNew).click()

    def enterName(self, name):
        self.driver.find_element(*self.txtName).send_keys(name)

    def clickOnSave(self):
        self.driver.find_element(*self.btnSave).click()