from Tests.BaseWrapper.Driver import DriverWrapper


class SupplierDetails(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    REFRESH_CATALOG_BUTTON_CSS = '.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.MuiButton-outlinedPrimary' \
                                 '.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge'
    SUPPLIER_ACCOUNT_CURRENCY_AMOUNT_XPATH = '/tr/following-sibling::td[2][contains(text(), ' \
                                             '"{0}")]/following-sibling::td[1]'
    SUPPLIERS_ACCOUNTS_XPATH = f'//h3[contains(text(), "My Accounts")]//tbody{SUPPLIER_ACCOUNT_CURRENCY_AMOUNT_XPATH}'
    SUPPLIER_ACCOUNTS_CURRENCIES_XPATH = 'td[value="{0}"]'
    PRODUCT_CONFIGURATION_BY_ID_XPATH = '/tr/td[1][contains(text(),"{0}")]'
    PRODUCT_CONFIGURATION_XPATH = f'//h3[contains(text(), "Product Configurations")]//tbody' \
                                  f'{PRODUCT_CONFIGURATION_BY_ID_XPATH} '
    PRODUCT_CONFIGURATIONS_XPATH = '//h3[contains(text(), "Product Configurations")]//tbody/tr/td[1]'
    PRODUCT_CONFIGURATIONS_ROWS_XPATH = '//h3[contains(text(), "Product ' \
                                        'Configurations")]//tbody/tr[{0}]/td[{1}] '
    ID_COLUMN_NUMBER = '1'
    COUNTRY_COLUMN_NUMBER = '2'
    FACE_VALUE_COLUMN_NUMBER = '3'
    CURRENCY_COLUMN_NUMBER = '4'
    SUPPLIER_PRICE_COLUMN_NUMBER = '5'
    PRICE_CURRENCY_COLUMN_NUMBER = '6'
    ACTIONS_COLUMN_NUMBER = '7'
    EDIT_CONFIGURATION_BUTTON_XPATH = f'{PRODUCT_CONFIGURATIONS_ROWS_XPATH}/button[1]'
    DELETE_CONFIGURATION_BUTTON_XPATH = f'{PRODUCT_CONFIGURATIONS_ROWS_XPATH}/button[2]'
    RELATE_ID_BUTTON_CSS = 'button:nth-child(2)..MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton' \
                           '-textPrimary.MuiButton-textSizeLarge.MuiButton-sizeLarge '
    EDIT_SUPPLIER_BUTTON = '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary' \
                           '.MuiButton-containedSizeLarge.MuiButton-sizeLarge '

    def find_product_config_row_num(self, config_id):
        product_configurations = self.search_elements_by_xpath(self.PRODUCT_CONFIGURATIONS_XPATH)
        row_number = 0
        for config in product_configurations:
            row_number += 1
            if config.text == config_id:
                return row_number

    def check_product_config_details(self, config_id, exp_country='Not specified', exp_face_value='Not specified',
                                     exp_currency='Not specified', exp_supp_price='Not specified',
                                     exp_price_currency='Not specified'):
        row_num = self.find_product_config_row_num(config_id)
        country_text = 'Not specified'
        currency_text = 'Not specified'
        face_value_text = 'Not specified'
        supp_price_text = 'Not specified'
        price_currency_text = 'Not specified'
        if exp_country != 'Not specified':
            country = self.search_element_by_xpath(self.PRODUCT_CONFIGURATIONS_ROWS_XPATH.format(
                row_num, self.COUNTRY_COLUMN_NUMBER))
            country_text = country.text
        if exp_currency != 'Not specified':
            currency = self.search_element_by_xpath(self.PRODUCT_CONFIGURATIONS_ROWS_XPATH.format(
                row_num, self.CURRENCY_COLUMN_NUMBER))
            currency_text = currency.text
        if exp_face_value != 'Not specified':
            face_value = self.search_element_by_xpath(self.PRODUCT_CONFIGURATIONS_ROWS_XPATH.format(
                row_num, self.FACE_VALUE_COLUMN_NUMBER))
            face_value_text = face_value.text
        if exp_supp_price != 'Not specified':
            supp_price = self.search_element_by_xpath(self.PRODUCT_CONFIGURATIONS_ROWS_XPATH.format(
                row_num, self.SUPPLIER_PRICE_COLUMN_NUMBER))
            supp_price_text = supp_price.text
        if exp_price_currency != 'Not specified':
            price_currency = self.search_element_by_xpath(self.PRODUCT_CONFIGURATIONS_ROWS_XPATH.format(
                row_num, self.PRICE_CURRENCY_COLUMN_NUMBER))
            price_currency_text = price_currency.text
        if country_text == exp_country and currency_text == exp_currency and face_value_text == exp_face_value and \
                supp_price_text == exp_supp_price and price_currency_text == exp_price_currency:
            return True
        else:
            return False

    def check_account_amount(self, currency):
        account = self.search_element_by_xpath(self.SUPPLIERS_ACCOUNTS_XPATH.format(currency))
        amount = account.text
        return amount

    def check_accounts_are_present(self, exp_acc_list):
        result = True
        for currency in exp_acc_list:
            status = self.check_elements_presents_css(self.SUPPLIER_ACCOUNTS_CURRENCIES_XPATH.format(currency))
            if not status:
                result = False
        return result



