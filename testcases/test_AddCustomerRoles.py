import pytest

from pageObjects.login import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomerRolesPage import AddCustomerRoles

class Test_003_CustomerRoles:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_AddCustomerRoles(self,setup):
        self.logger.info("***** Started: Test_003_CustomerRoles *****")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.logger.info("**** Login Successful ****")

        self.logger.info("*** Start Test_003_CustomerRoles ****")

        self.addcustomerroles= AddCustomerRoles(self.driver)
        self.addcustomerroles.clickOnCustomerMenu()
        self.addcustomerroles.clickOnCustomerRoles()
        self.addcustomerroles.clickOnAddNew()
        self.addcustomerroles.enterName("user1")
        self.addcustomerroles.clickOnSave()
        # // div[ @

        # class ='alert alert-success alert-dismissable']