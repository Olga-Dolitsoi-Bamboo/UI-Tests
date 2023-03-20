import time

from Tests.BaseWrapper.Driver import DriverWrapper


class AddClient(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator
    ADD_CLIENT_POPUP = '.MuiDialog-paper.MuiDialog-paperScrollPaper'
    POPUP = '.Dialog-paperScrollPaper'
    SEARCH_FIELD_NAME = 'search'
    CHECK_BOX_IN_ROW = f'{ADD_CLIENT_POPUP} tr:nth-child(1)>td:nth-child(1)>span'
    SAVE_CLIENTS_BUTTON = '//span[contains(text(), "Save edits")]/..'

    def search_client(self, client_name):
        popup = self.search_element_by_css(self.ADD_CLIENT_POPUP)
        field = popup.find_element_by_name(self.SEARCH_FIELD_NAME)
        self.input_into_element(field, client_name)

    def add_client(self, client_name):
        self.search_client(client_name)
        checkbox = self.search_element_by_css(self.CHECK_BOX_IN_ROW)
        self.click_on_element(checkbox)
        time.sleep(3)
        popup = self.search_element_by_css(self.POPUP)
        popup.find_element_by_xpath(self.SAVE_CLIENTS_BUTTON)


