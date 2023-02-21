from Tests.BaseWrapper.Driver import DriverWrapper


class BulkEditBrand(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_FIELD_NAME = 'searchText'
    DEACTIVATE_SWITCH_CSS = 'button[value="inactive"]'
    ACTIVATE_SWITCH_CSS = 'button[value="active"]'
    ADD_CATALOG_BUTTON_XPATH = '//button/span[contains(text(), "Add Catalog")]'
    REMOVE_FROM_CATALOG_BUTTON = '//button/span[contains(text(), "Remove")]'
    CATALOG_CHECKBOX_XPATH = '//td[contains(text(), "{0}")]/preceding-sibling::td[1]//input'
    ACTIONS_WITH_CATALOGS_XPATH = '//tr/td[contains(text(), "{0}")]/following-sibling::tr[8]'
    EDIT_CATALOG_XPATH = f'{ACTIONS_WITH_CATALOGS_XPATH}/button[@title="Edit"]'
    DELETE_CATALOG_XPATH = f'{ACTIONS_WITH_CATALOGS_XPATH}/button[title="Delete"]'
    ACTIVATE_CATALOG_SWITCH = '//tr/td[contains(text(), "{0}")]/following-sibling::td[7]/span[' \
                              '@class=".MuiSwitch-switchBase"]//input'
    SUPPLIER_FEE_VALUE_NAME = 'supplierPriceFeeValue'
    SUPPLIER_FEE_TYPE_CSS = 'input[placeholder="Supplier Fee Type"]'
    TRANSACTION_FEE_VALUE_NAME = 'supplierDiscountValue'
    TRANSACTION_FEE_TYPE_CSS = 'input[placeholder="Transaction Fee Type"]'
    DISCOUNT_VALUE_NAME = 'supplierDiscountValue'
    DISCOUNT_TYPE_CSS = 'input[placeholder="Discount Type"]'
    SAVE_EDITS_BUTTON_CSS = 'button[title="Save"]'
    CANCEL_EDIT_BUTTON_CSS = 'button[title="Cancel"]'
    ADD_CATALOG_TO_BRAND_POPUP_CSS = '.MuiPaper-elevation1'
    CHECKBOX_CATALOG_CSS = 'td:contains("{0}")~td>input'
    ACTIVATE_SELECTED_CATALOGS_TO_ADD_CSS = f'{ADD_CATALOG_TO_BRAND_POPUP_CSS} .MuiSwitch-input'
    SAVE_BRANDS_CATALOG_XPATH = 'span[contains(text(), "{0}")]'

    def search_catalog_by_text(self, catalog_name):
        self.input_in_search_field_name(self.SEARCH_FIELD_NAME, catalog_name)

    def select_catalog_with_checkbox(self, catalog_name):
        checkbox = self.search_element_by_xpath(self.CATALOG_CHECKBOX_XPATH.format(catalog_name))
        checkbox.click()

    def activate_catalog(self, catalog_name):
        self.select_catalog_with_checkbox(catalog_name)
        self.search_element_by_css(self.ACTIVATE_SWITCH_CSS).click()

    def activate_catalog_with_switch_button(self, catalog_name):
        self.search_element_by_xpath(self.ACTIVATE_CATALOG_SWITCH.format(catalog_name))

    def deactivate_catalog(self, catalog_name):
        self.select_catalog_with_checkbox(catalog_name)
        self.search_element_by_css(self.DEACTIVATE_SWITCH_CSS).click()

    def activate_all_selected_catalogs(self, catalogs_list):
        for catalog in catalogs_list:
            self.select_catalog_with_checkbox(catalog)
        self.search_element_by_css(self.ACTIVATE_SWITCH_CSS).click()

    def edit_catalog(self, catalog_name):
        edit_button = self.search_element_by_css(self.EDIT_CATALOG_XPATH.format(catalog_name))
        edit_button.click()

    def change_catalogs_parameter(self, catalog_name, params):
        self.edit_catalog(catalog_name)
        if params['Supp Fee Val'] != '':
            self.input_in_search_field_name(self.SUPPLIER_FEE_VALUE_NAME, params['Supp Fee Val'])
        if params['Supp Fee Type'] != '':
            self.dropdown_input_css(self.SUPPLIER_FEE_TYPE_CSS, params['Supp Fee Type'])
        if params['Trans Fee Val'] != '':
            self.input_in_search_field_name(self.TRANSACTION_FEE_VALUE_NAME, params['Trans Fee Val'])
        if params['Trans Fee Type'] != '':
            self.dropdown_input_css(self.TRANSACTION_FEE_TYPE_CSS, params['Trans Fee Type'])
        if params['Disk Val'] != '':
            self.input_in_search_field_name(self.DISCOUNT_VALUE_NAME, params['Disk Val'])
        if params['Disk Type'] != '':
            self.dropdown_input_css(self.DISCOUNT_TYPE_CSS, params['Disk Type'])
        self.search_element_by_css(self.SAVE_EDITS_BUTTON_CSS).click()

    def save_brands_catalog(self):
        self.search_element_by_xpath(self.SAVE_BRANDS_CATALOG_XPATH).click()


