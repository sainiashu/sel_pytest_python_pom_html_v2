import pytest
from selenium import  webdriver


@pytest.fixture
def setup(browser):
    if browser == 'is':
        driver = webdriver.ie()
        print('Launching ie browser')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print('Launching Firefox browser')
    else:
        driver = webdriver.Chrome()
    return driver

    # driver.maximize_window()
    # return driver

def pytest_addoption(parser):    #This will get the value from the cli/hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## It is hook for adding environment info to html report
def pytest_configure(config):
    if hasattr(config, 'metadata'):
        config.metadata['Project Name'] = 'Pytest Learning'
        config.metadata['Module Name'] = 'Login'
        config.metadata['Tester Name'] = 'Demo'

#it is hook for delete and modify the html report
#@pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(config):
    if hasattr(config, 'metadata'):
        config.metadata.pop("JAVA_HOME", None)
        config.metadata.pop("Plugins",None)

