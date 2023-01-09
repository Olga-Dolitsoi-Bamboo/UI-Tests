from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class DriverWrapper:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.waiter = wait_time

    TEXT_SEARCH = '//{0}[contains(text(), "{1}")]'

    def click_the_button_css(self, locator):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element_by_css_selector(locator)
            element.click()
        except NoSuchElementException:
            print('Element located {0} not found'.format(locator))

    def input_in_search_field_name(self, name, text):
        try:
            WebDriverWait(self.driver, self.waiter).until(ec.visibility_of_element_located((By.NAME, name)))
            element = self.driver.find_element(By.NAME, name)
            element.clear()
            element.click()
            element.send_keys(text)
        except NoSuchElementException:
            print('Element located {0} not found'.format(name))

    def input_in_search_field_css(self, locator, text):
        try:
            WebDriverWait(self.driver, self.waiter).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            element.clear()
            element.click()
            element.send_keys(text)
        except NoSuchElementException:
            print('Element located {0} not found'.format(locator))

    def clear_fild_css(self, locator):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            element.clear()
        except NoSuchElementException:
            print('Element located {0} not found'.format(locator))

    def search_element_by_text(self, tag, text):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.XPATH, self.TEXT_SEARCH.format(tag, text))))
            element = self.driver.find_element(By.XPATH, self.TEXT_SEARCH.format(tag, text))
            return element
        except NoSuchElementException:
            print('Element with text {0} not found'.format(text))

    def find_all_elements_by_css(self, locator):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_elements(By.CSS_SELECTOR, locator)
            return element
        except NoSuchElementException:
            print('Element located {0} not found'.format(locator))

    def get_element_text_by_css(self, locator):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            elements_text = element.text
            return elements_text
        except NoSuchElementException:
            print('Element located {0} not found'.format(locator))

    def get_elements_by_tag_name(self, tag):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_all_elements_located((By.TAG_NAME, tag)))
            element = self.driver.find_elements(By.TAG_NAME, tag)
            return element
        except NoSuchElementException:
            print('Element  located {0} not found'.format(tag))

    def get_element_by_id(self, element_id):
        try:
            WebDriverWait(self.driver, self.waiter).until(ec.visibility_of_element_located((By.ID, element_id)))
            element = self.driver.find_element(By.ID, element_id)
            return element
        except NoSuchElementException:
            print('Element  located {0} not found'.format(element_id))

    def click_element_by_id(self, element_id):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.ID, element_id)))
            element = self.driver.find_element(By.ID, element_id)
            element.click()
        except NoSuchElementException:
            print('Element  located {0} not found'.format(element_id))

    def scroll_to_the_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def is_on_page_text(self, tag, text):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.XPATH, self.TEXT_SEARCH.format(tag, text))))
            element = self.driver.find_element(By.XPATH, self.TEXT_SEARCH.format(tag, text))
            return element.is_displayed()
        except NoSuchElementException:
            print('Element  with text {0} not found'.format(text))

    def follow_linked_text(self, text):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.LINK_TEXT, text)))
            element = self.driver.find_element(By.LINK_TEXT, text)
            element.click()
        except NoSuchElementException:
            print('Element with text "{0} is not on page"')

    def search_element_by_css(self, locator):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            return element
        except NoSuchElementException:
            print('Element  located {0} not found'.format(locator))

    def search_elements_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_all_elements_located((By.XPATH, xpath)))
            elements = self.driver.find_elements(By.XPATH, xpath)
            return elements
        except NoSuchElementException:
            print('Elements  located {0} not found'.format(xpath))

    def check_elements_presents_css(self, locator):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            return element.is_displayed()
        except NoSuchElementException:
            print('Elements  located {0} not found'.format(locator))





