from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.Brands.CreateNewBrandPopup import CreateNewBrand


class BrandDetails(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    BRAND_CURRENCY_XPATH = '//div[contains(text(), "Currency")]/following-sibling::div'
    BRAND_SUPPLIER_XPATH = '//div[contains(text(), "Supplier")]/following-sibling::div'
    BRAND_REGION_XPATH = '//div[contains(text(), "Region")]/following-sibling::div'
    BRAND_INTERNAL_ID_XPATH = '//div[contains(text(), "Internal ID")]/div'
    AVAILABLE_DENOMINATIONS_XPATH = '//p[contains(text(), "Available denominations"/div/div'
    CHECK_PRODUCTS_LINKED_TEXT = 'a[href="/brands/53157/products"]>button'
    DELETE_BRAND_BUTTON_CSS = '.MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textSecondary.MuiButton' \
                              '-textSizeLarge.MuiButton-sizeLarge '
    EDIT_BRAND_BUTTON_CSS = '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary' \
                            '.MuiButton-containedSizeLarge.MuiButton-sizeLarge '
    LIVE_STATUS_SWITCHER_CSS = ''
    URL_BRAND_SWITCHER_CSS = ''
    DELETE_BRAND_POPUP = '.MuiPaper-elevation1.MuiPaper-rounded'
    DELETE_BUTTON_CSS = f'{DELETE_BRAND_POPUP}>button..MuiButtonBase-root.MuiButton-root.MuiButton-contained' \
                        f'.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge '
    CANCEL_DELETE_BUTTON = f'{DELETE_BRAND_POPUP}>button..MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton' \
                           f'-textSecondary.MuiButton-textSizeLarge.MuiButton-sizeLarge '

    def go_to_edit_brand(self):
        self.click_the_button_css(self.EDIT_BRAND_BUTTON_CSS)
        edit_popup = CreateNewBrand(self.driver)
        return edit_popup

    def change_status(self):
        self.click_the_button_css(self.LIVE_STATUS_SWITCHER_CSS)

    def change_url_brand(self):
        self.click_the_button_css(self.URL_BRAND_SWITCHER_CSS)

    def get_available_denominations(self):
        list_of_denominations = []
        list_of_elem = self.search_elements_by_xpath(self.AVAILABLE_DENOMINATIONS_XPATH)
        for elem in list_of_elem:
            list_of_denominations.append(elem.text)
        return list_of_denominations

    def check_brands_info(self, exp_currency, exp_region, exp_supplier):
        currency = self.search_element_by_xpath(self.BRAND_CURRENCY_XPATH)
        supplier = self.search_element_by_xpath(self.BRAND_SUPPLIER_XPATH)
        region = self.search_element_by_xpath(self.BRAND_REGION_XPATH)
        if currency.text == exp_currency and supplier.text == exp_supplier and region.text == exp_region:
            return True
        elif currency.text != exp_currency:
            print(f'{currency.text} is not equal {exp_currency}')
            return False
        elif supplier.text != exp_supplier:
            print(f'{supplier.text} is not equal {exp_supplier}')
            return False
        elif region.text != exp_region:
            print(f'{region.text} is not equal {exp_region}')
            return False

    def delete_brand(self):
        self.click_the_button_css(self.DELETE_BRAND_BUTTON_CSS)
        if self.check_is_present_css(self.DELETE_BRAND_POPUP):
            self.click_the_button_css(self.DELETE_BUTTON_CSS)


