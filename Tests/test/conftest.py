import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def app(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://dev.bamboocardportal.com/signin')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.get('chrome://settings/clearBrowserData')
    driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
    driver.close()


