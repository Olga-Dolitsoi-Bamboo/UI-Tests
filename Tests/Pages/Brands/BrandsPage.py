from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.Brands.CreateNewBrandPopup import CreateNewBrand


class Brands(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    SUPPLIER_FILTER_DROPDOWN_CSS = 'div[placeholder = "All Suppliers"]>div>div>input'
    REGIONS_FILTER_DROPDOWN_CSS = 'div[placeholder = "All Regions"]>div>div>input'
    CURRENCIES_FILTER_DROPDOWN_CSS = 'div[placeholder = "All Currencies"]>div>div>input'
    BRANDS_FILTER_DROPDOWN_CSS = 'div[placeholder = "All Brands"]>div>div>input'
    INTEGRATION_FILTER_DROPDOWN_CSS = 'div[placeholder = "Integration type"]>div>div>input'
    SEARCH_FIELD_NAME = 'searchText'
    ADD_NEW_BRAND_BUTTON = '.MuiButtonBase-root.MuiFab-root.MuiFab-extended.MuiFab-primary'
    BRANDS_BLOCK_CSS = '.infinite-scroll-component__outerdiv'
    BRAND_XPATH = '//div/div/a/div[2]/div[contains(text(), "{0}")]'
    BRAND_CSS = 'a>div:nth-child(2)>div'
    FIRST_BRAND_IN_LIST = 'a:nth-child(1)>div:nth-child(2)>div'

    def find_brand_with_search_field(self, brand_name):
        self.input_in_search_field_name(self.SEARCH_FIELD_NAME, brand_name)
        self.click_the_button_css(self.BRAND_CSS)

    def filter_brands_by_supplier(self, value):
        self.dropdown_input_css(self.SUPPLIER_FILTER_DROPDOWN_CSS, value)

    def filter_brands_by_currency(self, value):
        self.dropdown_input_css(self.CURRENCIES_FILTER_DROPDOWN_CSS, value)

    def filter_brand_by_region(self, value):
        self.dropdown_input_css(self.REGIONS_FILTER_DROPDOWN_CSS, value)

    def filter_brand_by_brand(self, value):
        self.dropdown_input_css(self.BRANDS_FILTER_DROPDOWN_CSS, value)

    def filter_brand_by_integration(self, is_integrated=True):
        if is_integrated:
            self.dropdown_input_css(self.INTEGRATION_FILTER_DROPDOWN_CSS, 'Api')
        elif not is_integrated:
            self.dropdown_input_css(self.INTEGRATION_FILTER_DROPDOWN_CSS, 'Manual')

    def go_to_brand_by_name(self, name):
        brand = self.search_element_by_text('div', name)
        brand.click()

    def is_brand_in_list(self, name):
        self.check_is_present_text('div', name)

    def go_to_brand_after_filtering(self, br_name):
        brands = self.find_all_elements_by_css(self.BRAND_CSS)
        for brand in brands:
            if brand.text == br_name:
                brand.click()
            else:
                'No such brand for this conditions'

    def go_to_create_brand(self):
        button = self.search_element_by_css(self.ADD_NEW_BRAND_BUTTON)
        self.press_selected_place_of_elem(button, 137.2, 24.5)
        create_brand_popup = CreateNewBrand(self.driver)
        return create_brand_popup




