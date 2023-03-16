"""Elements and methods for menu options"""
import time

from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Constants import SearchText as s_text


class Menu(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    MENU_LIST_CSS = '.jss49'
    MENU_OPTION_CSS = 'jss272'
    SUBLIST_CSS = '.MuiCollapse-wrapperInner'
    EXPANDED_OPTION_CSS = 'MuiSvgIcon-root.jss26.jss27'
    EXPAND_BUTTON_XPATH = '//div[contains(text(), {1})]/following-sibling::svg'
    BAMBOO_LOGO_CSS = 'div.jss88'

    @property
    def is_on_portal(self):
        return self.check_elements_presents_css(self.MENU_LIST_CSS)

    def get_menu_list(self):
        menu_list = self.find_all_elements_by_css(self.MENU_OPTION_CSS)
        return menu_list

    def check_menu_list_elements(self):
        list_elements = self.get_menu_list()
        names_list = []
        expected_names_list = [s_text.ORDERS_TEXT[0], s_text.PRODUCTS_TEXT[0], s_text.SUPPLIERS_TEXT[0],
                               s_text.FINANCE_TEXT[0], s_text.CLIENTS_TEXT[0], s_text.MARKETPLACES_TEXT[0],
                               s_text.REPORTS_TEXT[0], s_text.ANALYTICS_TEXT[0], s_text.USERS_TEXT[0]]
        for element in list_elements:
            names_list.append(element.text)
        if names_list == expected_names_list:
            return True
        else:
            return False

    def expand_options(self, option_name):
        orders_dropdown = self.search_element_by_text('div', option_name[0])
        orders_dropdown.click()

    def is_option_expanded(self, option_name):
        following_elements = self.search_elements_by_xpath(self.EXPAND_BUTTON_XPATH.format(option_name[1],
                                                                                           option_name[0]))
        answer: bool = False
        for element in following_elements:
            if element.get_attribute('class') == self.EXPANDED_OPTION_CSS:
                answer = True
        return answer

    def go_to_option(self, option_name):
        option = self.search_element_by_text(option_name[1], option_name[0])
        option.click()
        time.sleep(10)

    def is_on_some_page(self, option_url):
        url = self.driver.current_url
        return option_url == url.rsplit('/', 1)[-1]

    def scroll_to_sub_option(self, option_text):
        option = self.search_element_by_text('a', option_text)
        self.scroll_to_the_element(option)
