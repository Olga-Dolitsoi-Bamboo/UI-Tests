from Tests.BaseWrapper.Driver import DriverWrapper


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
    INVOICE_FREQUENCY_CSS = 'div[name="invoiceFrequency"]>div>div>input'
    CONFIRMATION_BUTTON_CSS = 'button[type="submit"]'

    def fill_basic_client_info(self, name, rate, integration, structure, settlement, account, invoice):
        self.input_in_search_field_name(self.NAME_FIELD_NAME, name)
        self.input_in_search_field_name(self.EXCHANGE_FIELD_NAME, rate)
        self.dropdown_input_css(self.TYPE_FIELD_CSS, integration)
        self.dropdown_input_css(self.COMMERCIAL_FIELD_CSS, structure)
        self.dropdown_input_css(self.SETTLEMENT_FIELD_CSS, settlement)
        self.dropdown_input_css(self.ACCOUNT_FIELD_CSS, account)
        self.dropdown_input_css(self.INVOICE_FREQUENCY_CSS, invoice)
        submit_button = self.search_element_by_css(self.CONFIRMATION_BUTTON_CSS)
        self.scroll_to_the_element(submit_button)
        submit_button.click()

    def create_client(self, name, rate, integration, structure, settlement, account, invoice):
        self.fill_basic_client_info(name, rate, integration, structure, settlement, account, invoice)

    def edit_client_options(self, name='', rate='', integration='', structure='', settlement='',
                            account='', auto_inv=''):
        option_list = [[name, self.NAME_FIELD_NAME, 'name'], [rate, self.EXCHANGE_FIELD_NAME, 'name'],
                       [integration, self.TYPE_FIELD_CSS, 'css'], [structure, self.COMMERCIAL_FIELD_CSS, 'css'],
                       [settlement, self.SETTLEMENT_FIELD_CSS, 'css'], [account, self.ACCOUNT_FIELD_CSS, 'css'],
                       [auto_inv, self.INVOICE_FREQUENCY_CSS, 'css']]
        for options in option_list:
            if options[0] != '':
                if options[2] == 'name':
                    self.input_in_search_field_name(options[1], options[0])
                elif options[2] == 'css':
                    self.dropdown_input_css(options[1], options[0])
        submit_button = self.search_element_by_css(self.CONFIRMATION_BUTTON_CSS)
        self.scroll_to_the_element(submit_button)
        submit_button.click()

    def check_error_message_name(self, error_message):
        return self.check_is_present_xpath(self.TEXT_SEARCH.format('p', error_message))



