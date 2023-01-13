from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.Clients.ClientDetailPage import ClientDetails


class Clients(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    GO_TO_PREVIOUS_PAGE_BUTTON_CSS = '.MuiButtonBase-root.MuiPaginationItem-root.MuiPaginationItem-page[]'
    GO_TO_NEXT_PAGE_BUTTON_CSS = '.MuiButtonBase-root.MuiPaginationItem-root.MuiPaginationItem-page[]'
    GO_TO_NUMBER_PAGE_CSS = '.MuiButtonBase-root.MuiPaginationItem-root.MuiPaginationItem-page[aria-label="Go to page ' \
                            '{0}]" '
    CURRENT_PAGE_CSS = '.MuiButtonBase-root.MuiPaginationItem-root.MuiPaginationItem-page[aria-label="page {0}"]'
    CLIENT_ROW_CSS = '.MuiTableRow-root.MuiTableRow-hover'
    CLIENT_NAME_CSS = f'{CLIENT_ROW_CSS} > td:nt-child(1).MuiTableCell-root.MuiTableCell-body.MuiTableCell-alignLeft'
    CLIENT_BY_NAME_XPATH = '//tbody/tr/td[contains(text(), "{0}")]'
    ADD_CLIENT_BUTTON_CSS = '#table-client-list button'
    SEARCH_FIELD_NAME = 'search'
    ACCOUNT_TYPE_CSS = 'input[placeholder="Account Type"]'
    ACCOUNT_STATUS_CSS = 'input[placeholder="Account Status"]'
    EXACT_NAME_CLIENT_CSS = f'tr:nth-child(1){CLIENT_ROW_CSS}'
    PAGE_SWITCHERS_CSS = '.MuiPaginationItem-page'
    PAGE_CSS = '#table-client-list'

    def go_to_create_clients(self):
        self.wait_page_elements_presents(self.PAGE_CSS)
        button = self.driver.find_element(By.CSS_SELECTOR, self.ADD_CLIENT_BUTTON_CSS)
        self.press_selected_place_of_elem(button, 133, 48)

    def go_to_page_by_num(self, number):
        self.click_the_button_css(self.GO_TO_NUMBER_PAGE_CSS.format(number))

    def go_to_client_by_search(self, search_text):
        self.input_in_search_field_name(self.SEARCH_FIELD_NAME, search_text)
        exact_client = self.click_the_button_css(self.EXACT_NAME_CLIENT_CSS)
        exact_client.click()

    def find_client_in_list(self, client_name):
        names_list = self.find_all_elements_by_css(self.CLIENT_NAME_CSS)
        my_client: str
        for names in names_list:
            if names.text == client_name:
                return names

    def check_client_in_list(self, client_name):
        in_list = False
        names_lists = []
        next_button = self.search_element_by_css(self.GO_TO_NEXT_PAGE_BUTTON_CSS)
        pages = self.find_all_elements_by_css(self.PAGE_SWITCHERS_CSS)
        number_of_pages = len(pages) - 3
        for num in range(0, number_of_pages):
            names_page = self.find_all_elements_by_css(self.CLIENT_NAME_CSS)
            names_lists.append(names_page)
            for names in names_page:
                if names.text == client_name:
                    in_list = True
                    names.click()
                    client_details = ClientDetails(self.driver)
                    return client_details
            if not in_list:
                next_button.click()

    def go_to_client(self, client_name):
        client = self.find_client_in_list(client_name)
        client.click()
        client_details = ClientDetails(self.driver)
        return client_details

    def go_to_client_by_name(self, name_cl):
        client = self.search_element_by_xpath(self.CLIENT_BY_NAME_XPATH.format(name_cl))
        WebDriverWait(self.driver, self.waiter).until(
            ec.element_to_be_clickable((By.XPATH, self.CLIENT_BY_NAME_XPATH.format(name_cl))))
        self.scroll_to_the_element(client)
        client.click()
        client_details = ClientDetails(self.driver)
        return client_details
