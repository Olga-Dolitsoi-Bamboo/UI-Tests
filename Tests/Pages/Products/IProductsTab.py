from Tests.BaseWrapper.Driver import DriverWrapper


class IntegratedProducts(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    EDIT_PRODUCTS_BUTTON_CSS = '.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.MuiButton-outlinedPrimary' \
                               '.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge '
    NEXT_PAGE_BUTTON_CSS = 'button[aria-label="Go to next page"]'
    PREVIOUS_PAGE_BUTTON_CSS = 'button[aria-label="Go to previous page"]'
    GO_TO_PAGE_BY_NUMBER_CSS = 'button[aria-label="Go to page {0}"]'

    PRODUCT_ROW_BY_SKU_NAME_XPATH = '//tbody//tr/td[{0}][@value="{1}"]'
    NAME_COLUMN_NUMBER = 5
    SKU_COLUMN_NUMBER = 1
    STATUS_COLUMN_NUMBER = 'td[-2]'
    EDIT_EXACT_PRODUCT_CSS = 'button[title="Edit"]'
    DELETE_EXACT_PRODUCT_CSS = 'button[title="Delete"]'
    ACTIVE_STATUS_CHECKBOX_CSS = 'input[name="isActive"]'
    PRODUCT_NAME_INPUT_FIELD = 'input[name="productName"]'
    SAVE_PRODUCTS_EDIT_FLAG_CSS = '.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-colorInherit:nth-of-type(1)'
    CANCEL_PRODUCTS_EDITS_FLAG_CSS = '.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-colorInherit:nth-of-type(2)'
    ADD_BRAND_TO_CATALOG_BUTTON_CSS = '.MuiGrid-grid-md-2'
    ADD_PRODUCT_TO_CATALOG_BUTTON_CSS = '.MuiGrid-grid-md-1'
    CANCEL_EDITS_BUTTON_CSS = '.MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textSecondary' \
                              '.MuiButton-textSizeLarge.MuiButton-sizeLarge'
    SAVE_EDITS_BUTTON_CSS = '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary' \
                            '.MuiButton-containedSizeLarge.MuiButton-sizeLarge'
    ELEMENT_IN_PRODUCT_ROW = 'tr[{0}] > {1}'
    INTEGRATED_PRODUCTS_TAB_CSS = 'button[role="tab"]:nth-of-type(1)'

    @staticmethod
    def for_edit_tab(column_number):
        column_number += 1
        return str(column_number)

    def find_product_row(self, identifier, is_edit=True, by_sku=True):
        locator = ''
        if is_edit:
            if by_sku:
                locator = self.PRODUCT_ROW_BY_SKU_NAME_XPATH.format([self.for_edit_tab(self.SKU_COLUMN_NUMBER),
                                                                     identifier])
            elif not by_sku:
                locator = self.PRODUCT_ROW_BY_SKU_NAME_XPATH.format([self.for_edit_tab(self.NAME_COLUMN_NUMBER),
                                                                     identifier])
        elif not is_edit:
            if by_sku:
                locator = self.PRODUCT_ROW_BY_SKU_NAME_XPATH.format([self.SKU_COLUMN_NUMBER, identifier])
            elif not by_sku:
                locator = self.PRODUCT_ROW_BY_SKU_NAME_XPATH.format([self.NAME_COLUMN_NUMBER, identifier])
        row_elem = self.search_element_by_xpath(locator)
        row = row_elem.find_element_by_xpath('..')
        return row

    def go_to_edit_product(self, product_identifier, is_sku=True):
        self.click_the_button_css(self.EDIT_PRODUCTS_BUTTON_CSS)
        row = self.find_product_row(product_identifier, is_edit=True, by_sku=is_sku)
        edit_button = row.find_element_by_css_selector(self.EDIT_EXACT_PRODUCT_CSS)
        edit_button.click()
        return row

    def change_product_name(self, identifier, new_name, is_sku=True):
        row = self.go_to_edit_product(identifier, is_sku=is_sku)
        self.input_in_search_field_css(self.PRODUCT_NAME_INPUT_FIELD, new_name)
        save_btn = row.find_element_by_css_selector(self.SAVE_PRODUCTS_EDIT_FLAG_CSS)
        save_btn.click()

    def change_product_status(self, identifier, is_sku=True):
        row = self.go_to_edit_product(identifier, is_sku=is_sku)
        row.find_element_by_css_selector(self.ACTIVE_STATUS_CHECKBOX_CSS).click()
        save_btn = row.find_element_by_css_selector(self.SAVE_PRODUCTS_EDIT_FLAG_CSS)
        save_btn.click()

    def check_status_changed(self, identifier, is_sku=True, expected_status=True):
        row = self.find_product_row(identifier, is_edit=False, by_sku=is_sku)
        if expected_status:
            if row.find_element_by_css_selector(self.STATUS_COLUMN_NUMBER).get_attribute("value") == "true":
                return True
            else:
                return False
        elif not expected_status:
            if row.find_element_by_css_selector(self.STATUS_COLUMN_NUMBER).get_attribute("value") == "false":
                return True
            else:
                return False

    def check_any_product_value(self, identifier, col_num, exp_value, is_sku=True):
        row = self.find_product_row(identifier, is_edit=False, by_sku=is_sku)
        actual_value = row.find_element_by_css_selector('td[{0}]'.format(col_num)).get_atribute("value")
        if exp_value == actual_value:
            return True
        else:
            return False


