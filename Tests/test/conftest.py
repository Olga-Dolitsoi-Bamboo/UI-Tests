import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pypyodbc as odbc
from Constants import DataBase as my_dbo


@pytest.fixture()
def my_app():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


@pytest.fixture(autouse=True)
def app(my_app):
    my_app.get('https://dev.bamboocardportal.com/signin')
    my_app.implicitly_wait(3)
    my_app.maximize_window()
    yield
    my_app.get('chrome://settings/clearBrowserData')
    my_app.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
    #clean_db()
    my_app.close()


def clean_db():
    my_bd = odbc.connect(connectString=my_dbo.connection_string)
    cursor = my_bd.cursor()
    cursor.execute(my_dbo.CLIENT_QUERY)
    my_bd.commit()
    cursor.execute(my_dbo.BRANDS_QUERY)
    my_bd.commit()
    cursor.execute(my_dbo.PRODUCTS_QUERY)
    my_bd.commit()
    cursor.execute(my_dbo.CATALOG_QUERY)
    my_bd.commit()
    cursor.execute(my_dbo.CATALOG_CLIENT_QUERY)
    my_bd.commit()
