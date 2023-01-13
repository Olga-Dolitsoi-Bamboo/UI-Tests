from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.Clients.ClientsPage import Clients


class CreateClient(DriverWrapper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    NAME_FIELD_NAME = 'name'
    EXCHANGE_FIELD_NAME = 'exchangeCommission'
    TYPE_FIELD_CSS = 'div[name="integrationType"]>div>div>input'
    COMMERCIAL_FIELD_CSS = 'div[name="commercialStructure"]>div>div>input'
    SETTLEMENT_FIELD_CSS = 'div[name="settlementMethod"]>div>div>input'
    ACCOUNT_FIELD_CSS = 'div[name="accountType"]>div>div>input'
    CONFIRMATION_BUTTON_CSS = 'button[type="submit"]'

    def fill_basic_client_info(self, name, rate, integration, structure, settlement, account):
        self.input_in_search_field_name(self.NAME_FIELD_NAME, name)
        self.input_in_search_field_name(self.EXCHANGE_FIELD_NAME, rate)
        self.dropdown_input_css(self.TYPE_FIELD_CSS, integration)
        self.dropdown_input_css(self.COMMERCIAL_FIELD_CSS, structure)
        self.dropdown_input_css(self.SETTLEMENT_FIELD_CSS, settlement)
        self.dropdown_input_css(self.ACCOUNT_FIELD_CSS, account)
        submit_button = self.search_element_by_css(self.CONFIRMATION_BUTTON_CSS)
        self.scroll_to_the_element(submit_button)
        submit_button.click()

    def create_client(self, name, rate, integration, structure, settlement, account):
        self.fill_basic_client_info(name, rate, integration, structure, settlement, account)
        cl_page = Clients(self.driver)
        return cl_page
