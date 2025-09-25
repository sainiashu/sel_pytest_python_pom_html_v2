import  pytest
from selenium import  webdriver
from pageObjects.login import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_login:
    baseURL= ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    loggen = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.loggen.info("XXXXXXXXXXXXXX Test_001_login XXXXXXXXXXXXXX")
        self.loggen.info("XXXXXXXXXXXXXX test_homePageTitle XXXXXXXXXXXXXX")
        self.driver = setup
        self.driver.get(self.baseURL)
        actualTitle = self.driver.title


        if actualTitle == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.loggen.info("XXXXXXXXXXXXXX Test Passed XXXXXXXXXXXXXX")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert  False
            self.loggen.info("XXXXXXXXXXXXXX Test Failed XXXXXXXXXXXXXX")

    @pytest.mark.regression
    def test_login(self, setup):
        self.loggen.info("XXXXXXXXXXXXXX Test_001_login XXXXXXXXXXXXXX")
        self.loggen.info("XXXXXXXXXXXXXX test_login XXXXXXXXXXXXXX")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.loggen.info("XXXXXXXXXXXXXX Test Passed XXXXXXXXXXXXXX")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.driver.close()
            self.loggen.info("XXXXXXXXXXXXXX Test Failed XXXXXXXXXXXXXX")