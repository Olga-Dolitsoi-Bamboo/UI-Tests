import time

from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.Clients.CreateClientPopup import CreateClient


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
    ADD_ACCOUNT_BUTTON_TEXT = 'Add account'
    ACTIVE_STATUS_SWITCH_NAME = 'liveStatus'
    DELETE_CLIENT_BUTTON_CSS = 'button:nth-child(3).MuiButton-textSizeLarge.MuiButton-sizeLarge'
    EDIT_CLIENT_BUTTON_CSS = '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary' \
                             '.MuiButton-containedSizeLarge.MuiButton-sizeLarge '
    ACCOUNT_POPUP_CURRENCY_CSS = 'input[placeholder="Currency"]'
    ACCOUNT_POPUP_STATUS_CSS = 'input[placeholder="Status"]'
    CONFIRM_ACCOUNT_BUTTON_CSS = 'button[type="submit"]'
    ACCOUNT_ACTION_BUTTON_CSS = 'tr:nth-child({0})>td>div.accountActionsWrapper'
    CURRENCY_ROW_CSS = 'tr>td:nth-child(4)'
    EDIT_ACCOUNT_BUTTON_CSS = 'tr:nth-child({0})>td>.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-colorInherit'
    THRESHOLD_INPUT_CSS = 'td>input[placeholder="Min Balance Threshold"]'
    XERO_ACCOUNT_INPUT_CSS = 'td>input[placeholder="Xero Accounts"]'
    SAVE_EDIT_ACC_BUTTON_CSS = 'button:nth-child(1).MuiButtonBase-root.MuiIconButton-root.MuiIconButton-colorInherit'
    CANCEL_EDIT_ACC_BUTTON_CSS = 'button:nth-child(2).MuiButtonBase-root.MuiIconButton-root.MuiIconButton-colorInherit'
    ACCOUNT_STATUS_CSS = 'tr:nth-child({0})>td:nth-child(9)'

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
        time.sleep(3)
        integration = self.search_element_by_xpath(self.ATTRIBUTE_XPATH.format(self.INTEGRATION_TEXT))
        status = self.search_element_by_xpath(self.ATTRIBUTE_XPATH.format(self.STATUS_TEXT))
        commission = self.search_element_by_xpath(self.ATTRIBUTE_XPATH.format(self.CLIENT_COMMISSION_TEXT))
        if integration.text == exp_integration and status.text == exp_status and commission.text == exp_commission:
            return True
        else:
            return False

    def go_to_edit_client(self):
        self.click_the_button_css(self.EDIT_CLIENT_BUTTON_CSS)
        edit_client = CreateClient(self.driver)
        return edit_client

    def change_status(self):
        self.click_the_button_css(self.ACTIVE_STATUS_SWITCH_NAME)

    def delete_client(self):
        self.click_the_button_css(self.DELETE_CLIENT_BUTTON_CSS)

    def add_account(self, currency, active=True):
        add_button = self.search_parent_by_xpath(self.TEXT_SEARCH.format('span', self.ADD_ACCOUNT_BUTTON_TEXT))
        add_button.click()
        time.sleep(2)
        self.dropdown_input_css(self.ACCOUNT_POPUP_CURRENCY_CSS, currency)
        if active:
            self.dropdown_input_css(self.ACCOUNT_POPUP_STATUS_CSS, 'Live')
        else:
            self.dropdown_input_css(self.ACCOUNT_POPUP_STATUS_CSS, 'Inactive')
        self.click_the_button_css(self.CONFIRM_ACCOUNT_BUTTON_CSS)

    def activate_account(self, currency):
        num_of_row = self.find_account_row(currency)
        self.click_the_button_css(self.ACCOUNT_ACTION_BUTTON_CSS.format(num_of_row))
        self.search_element_by_text('li', 'Activate')

    def find_account_row(self, currency):
        rows = self.find_all_elements_by_css(self.CURRENCY_ROW_CSS)
        row_num = 0
        for row in rows:
            row_num += 1
            if row.text == currency:
                return row_num
            elif row_num == len(rows):
                return 'Account not found'

    def change_client_status(self):
        switch_status = self.search_element_by_name(self.ACTIVE_STATUS_SWITCH_NAME)
        switch_status.click()

    def edit_account(self, currency):
        num_of_row = self.find_account_row(currency)
        edit_acc_button = self.search_element_by_css(self.EDIT_ACCOUNT_BUTTON_CSS.format(num_of_row))
        edit_acc_button.click()

    def edit_account_threshold(self, threshold, currency):
        self.edit_account(currency)
        self.input_in_search_field_css(self.THRESHOLD_INPUT_CSS, threshold)

    def edit_account_xero(self, xero, currency):
        self.edit_account(currency)
        self.input_in_search_field_css(self.XERO_ACCOUNT_INPUT_CSS, xero)


