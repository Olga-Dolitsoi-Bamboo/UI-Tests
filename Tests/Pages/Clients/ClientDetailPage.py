from Tests.BaseWrapper.Driver import DriverWrapper


class ClientDetails(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    COMMERCIAL_STRUCTURE_TEXT = 'Commercial Structure'
    INTEGRATION_TEXT = 'Integration'
    STATUS_TEXT = 'Status'
    CREDENTIALS_TEXT = ''
    CLIENT_COMMISSION_TEXT = 'Client Commission'
    CATALOG_TEXT = 'Catalog'
    ATTRIBUTE_XPATH = '//div[contains(text(), "{0}")]/following-sibling::div[1]'
    ADD_ACCOUNT_BUTTON_CSS = '.jss626'
    ACTIVE_STATUS_SWITCH_NAME = 'liveStatus'
    DELETE_CLIENT_BUTTON_CSS = 'jss645'
    EDIT_CLIENT_BUTTON_CSS = '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary' \
                             '.MuiButton-containedSizeLarge.MuiButton-sizeLarge '
    ACCOUNT_POPUP_CURRENCY_CSS = 'input[placeholder="Currency"]'
    ACCOUNT_POPUP_STATUS_CSS = 'input[placeholder="Status"]'
    CONFIRM_ACCOUNT_BUTTON_CSS = 'button[type="submit"]'

    def check_commercial_structure(self, name):
        name_text = self.search_element_by_xpath(self.ATTRIBUTE_XPATH.format(str(self.COMMERCIAL_STRUCTURE_TEXT)))
        if name_text.text == name:
            return True

    def check_catalog(self, catalog_name):
        if self.check_is_present_xpath(self.ATTRIBUTE_XPATH.format(self.CATALOG_TEXT)):
            catalog = self.search_element_by_xpath(self.ATTRIBUTE_XPATH.format(self.CATALOG_TEXT))
            if catalog.text == catalog_name:
                return True
        else:
            return 'No Catalogs for this Client'

    def has_catalog(self):
        if self.check_is_present_xpath(self.ATTRIBUTE_XPATH.format(self.CATALOG_TEXT)):
            return True
        else:
            return False

    def check_other_attributes(self, exp_integration, exp_status, exp_commission):
        integration = self.search_element_by_xpath(self.ATTRIBUTE_XPATH.format(self.INTEGRATION_TEXT))
        status = self.search_element_by_xpath(self.ATTRIBUTE_XPATH.format(self.STATUS_TEXT))
        commission = self.search_element_by_xpath(self.ATTRIBUTE_XPATH.format(self.CLIENT_COMMISSION_TEXT))
        if integration.text == exp_integration and status.text == exp_status and commission.text == exp_commission:
            return True
        else:
            return False

    def edit_client(self):
        self.click_the_button_css(self.EDIT_CLIENT_BUTTON_CSS)

    def change_status(self):
        self.click_the_button_css(self.ACTIVE_STATUS_SWITCH_NAME)

    def delete_client(self):
        self.click_the_button_css(self.DELETE_CLIENT_BUTTON_CSS)

    def add_account(self, currency, active=True):
        self.click_the_button_css(self.ADD_ACCOUNT_BUTTON_CSS)
        self.input_in_search_field_css(self.ACCOUNT_POPUP_CURRENCY_CSS, currency)
        if active:
            self.input_in_search_field_css(self.ACCOUNT_POPUP_STATUS_CSS, 'Live')
        else:
            self.input_in_search_field_css(self.ACCOUNT_POPUP_STATUS_CSS, 'Inactive')
        self.click_the_button_css(self.CONFIRM_ACCOUNT_BUTTON_CSS)
