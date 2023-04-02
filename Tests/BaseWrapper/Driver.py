import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class DriverWrapper:
    def __init__(self, driver, wait_time=20):
        self.driver = driver
        self.waiter = wait_time

    TEXT_SEARCH = '//{0}[contains(text(), "{1}")]'

    def click_the_button_css(self, locator):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            element.click()
        except NoSuchElementException:
            print('Element located {0} not found'.format(locator))

    def input_in_search_field_name(self, name, text):
        try:
            WebDriverWait(self.driver, self.waiter).until(ec.element_to_be_clickable((By.NAME, name)))
            element = self.driver.find_element(By.NAME, name)
            element.clear()
            element.click()
            element.send_keys(text)
        except NoSuchElementException:
            print('Element located {0} not found'.format(name))

    def input_in_search_field_css(self, locator, text):
        try:
            WebDriverWait(self.driver, self.waiter).until(ec.presence_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            element.clear()
            element.click()
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print('Element located {0} not found'.format(locator))

    @staticmethod
    def input_in_element(element, text):
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

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
            WebDriverWait(self.driver, 30).until(
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
            WebDriverWait(self.driver, 30).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            self.driver.find_element(By.CSS_SELECTOR, locator)
            return True
        except NoSuchElementException:
            print('Elements  located {0} not found'.format(locator))
            return False

    def wait_page_elements_presents(self, locator):
        WebDriverWait(self.driver, self.waiter).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def press_selected_place_of_elem(self, elem, x, y):
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(elem, x, y)
        action.click()
        action.perform()

    def dropdown_input_css(self, locator, value):
        try:
            WebDriverWait(self.driver, self.waiter).until(ec.presence_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            element.clear()
            element.click()
            element.send_keys(value)
            element.send_keys(Keys.DOWN)
            element.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print('Element located {0} not found'.format(locator))

    def search_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            return element
        except NoSuchElementException:
            print('Elements  located {0} not found'.format(xpath))

    def check_is_present_css(self, locator):
        try:
            WebDriverWait(self.driver, 30).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            self.driver.find_element(By.CSS_SELECTOR, locator)
            return True
        except NoSuchElementException:
            return False

    def check_is_present_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            print(element.text)
            return True
        except NoSuchElementException:
            return False

    def check_is_present_name(self, name):
        try:
            self.driver.find_element(By.NAME, name)
        except NoSuchElementException:
            return False
        return True

    def check_is_present_id(self, my_id):
        try:
            self.driver.find_element(By.ID, my_id)
        except NoSuchElementException:
            return False
        return True

    def check_is_present_text(self, tag, text):
        try:
            self.driver.find_element(By.XPATH, self.TEXT_SEARCH.format(tag, text))
        except NoSuchElementException:
            return False
        return True

    def search_element_by_name(self, name):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.visibility_of_element_located((By.NAME, name)))
            element = self.driver.find_element(By.NAME, name)
            return element
        except NoSuchElementException:
            print('Elements  located {0} not found'.format(name))

    def cursor_on_element_css(self, locator):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            action = ActionChains(self.driver)
            action.move_to_element(element)
        except NoSuchElementException:
            print('Elements  located {0} not found'.format(locator))

    def cursor_on_element_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            action = ActionChains(self.driver)
            action.move_to_element(element)
        except NoSuchElementException:
            print('Elements  located {0} not found'.format(xpath))

    def search_parent_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            parent_element = element.find_element(By.XPATH, "..")
            return parent_element
        except NoSuchElementException:
            print('Elements  located {0} not found'.format(xpath))

    def scroll_inside_div_xpath(self, xpath, div_locator):
        try:
            WebDriverWait(self.driver, self.waiter).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, xpath)))
            WebDriverWait(self.driver, self.waiter).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, div_locator)))
            element = self.driver.find_element(By.XPATH, div_locator)
            div_element = self.driver.find_element(By.XPATH, xpath)
            actions = ActionChains(self.driver)
            actions.move_to_element(div_element)
            actions.move_to_element(element).perform()
        except NoSuchElementException:
            print('Elements  located {0} not found'.format(xpath))

    def scroll_to_element_script(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def input_into_element(element, text):
        element.clear()
        element.click()
        element.send_keys(text)

    def click_on_element(self, element):
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()
        action_chains.click().perform()

    def click_with_timeout(self, element):
        WebDriverWait(self.driver, self.waiter).until(
            ec.element_to_be_clickable((By.XPATH, element)))
        element.click()
