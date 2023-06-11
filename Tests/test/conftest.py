import argparse

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pypyodbc as odbc
from Tests.Constants import DataBase as my_dbo


@pytest.fixture()
def my_app():
    if 'JENKINS_HOME' in os.environ:
        chrome_options = Options()
        chrome_options.binary_location = r"/usr/bin/google-chrome-stable"
        chrome_options.add_argument('--headless')

        chromedriver_path = r"/home/olga/my-project/Tests/chromedriver"
        # Create a new Chrome webdriver instance with the specified Chromedriver binary path
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    else:
        # Running locally, use relative path to Chromedriver
        chromedriver_path = '/home/olga/PycharmProjects/UI-Tests/Tests/chromedriver'
        driver = webdriver.Chrome(executable_path=chromedriver_path)
    return driver


@pytest.fixture(autouse=True)
def app(my_app):
    my_app.get('https://dev.bamboocardportal.com/signin')
    my_app.implicitly_wait(3)
    my_app.maximize_window()
    yield
    my_app.delete_all_cookies()
    #
    # my_app.get('chrome://settings/clearBrowserData')
    # my_app.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
    # #clean_db()
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
