import pytest
from selenium import webdriver
from pageObjects.login import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    yield driver
    driver.quit()

def test_login(setup, username, password):
    login_page = LoginPage(setup)
    # login_page.login(username, password)
    # assert "dashboard" in setup.current_url.lower()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

