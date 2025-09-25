import time

import  pytest
from selenium import  webdriver
from pageObjects.login import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_ddt_Login:
    baseURL= ReadConfig.getApplicationUrl()
    path = ".//TestData//logintestdata.xlsx"
    loggen = LogGen.loggen()

    # @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.loggen.info("XXXXXXXXXXXXXX Test_001_login XXXXXXXXXXXXXX")
        self.loggen.info("XXXXXXXXXXXXXX test_login XXXXXXXXXXXXXX")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows= XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows', self.rows)

        lst_status = []  # Empty list

        for r in range(2, self.rows):
            self.user = XLUtils.readData(self.path,'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.enter_username(self.user)
            self.lp.enter_password(self.password)
            self.lp.click_login()
            time.sleep(5)

        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"

        if act_title == exp_title:
            if self.exp == "Pass":
                self.logger.info("Test Passed")
                self.lp.click_logout()
                time.sleep(5)
                lst_status.append("Pass")