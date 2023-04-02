import time

from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.Catalogs.AddCatalogPopup import AddCatalog
from Tests.Pages.Catalogs.CatalogDetailsPage import CatalogDetails


class Catalogs(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_FIELD_NAME = 'searchText'
    SUPPLIERS_DROPDOWN_CSS = 'div[placeholder = "All Suppliers"]>div>div>input'
    REGIONS_DROPDOWN_CSS = 'div[placeholder = "All Regions"]>div>div>input'
    BRANDS_DROPDOWN_CSS = 'div[placeholder = "All Brands"]>div>div>input'
    CLIENTS_DROPDOWN_CSS = 'div[placeholder = "All Brands"]>div>div>input'
    CATALOG_NAME_LINK_CSS = 'div[title = "{0}"]'
    CATALOG_XPATH = '//div[contains(text(), "{0}")]'
    CREATE_CATALOG_BUTTON = '.MuiFab-primary'
    ADDITIONAL_OPTIONS_CSS = f'{CATALOG_NAME_LINK_CSS} div>div>svg'
    CREATE_ORDER_OPTION_TEXT = 'Create order'
    DUPLICATE_CATALOG_OPTION_TEXT = 'Duplicate'
    DELETE_CATALOG_OPTION_TEXT = 'Delete'
    ADD_ALL_PRODUCTS_OPTION_TEXT = 'Add all products'
    EDIT_CATALOG_OPTION_CSS = 'Edit'
    ADD_CATALOG_BUTTON_SPAN_TEXT = 'Add new catalog'

    def click_create_catalog(self):
        button = self.search_element_by_text('span', self.ADD_CATALOG_BUTTON_SPAN_TEXT)
        self.click_on_element(button)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # create_button = self.search_element_by_css(self.CREATE_CATALOG_BUTTON)
        # self.press_selected_place_of_elem(create_button, 149, 0)
        add_catalog_popup = AddCatalog(self.driver)
        return add_catalog_popup

    def filter_catalogs_by_region(self, region):
        self.dropdown_input_css(self.REGIONS_DROPDOWN_CSS, region)

    def filter_catalogs_by_supplier(self, supplier):
        self.dropdown_input_css(self.SUPPLIERS_DROPDOWN_CSS, supplier)

    def filter_catalogs_by_brand(self, brand):
        self.dropdown_input_css(self.BRANDS_DROPDOWN_CSS, brand)

    def filter_catalogs_by_client(self, client):
        self.dropdown_input_css(self.CLIENTS_DROPDOWN_CSS, client)

    def go_to_catalog(self, catalog_name):
        catalog = self.search_element_by_css(self.CATALOG_NAME_LINK_CSS.format(catalog_name))
        catalog.click()
        catalog_details = CatalogDetails(self.driver)
        return catalog_details

    def verify_catalog_exist(self, catalog_name):
        result = self.check_is_present_xpath(self.CATALOG_XPATH.format(catalog_name))
        return result

    def duplicate_catalog(self, name):
        catalog_options = self.search_element_by_css(self.ADDITIONAL_OPTIONS_CSS.format(name))
        catalog_options.click()
        self.search_element_by_text('li', self.DUPLICATE_CATALOG_OPTION_TEXT).click()

    def create_order_from_catalog(self, name):
        catalog_options = self.search_element_by_css(self.ADDITIONAL_OPTIONS_CSS.format(name))
        catalog_options.click()
        self.search_element_by_text('li', self.CREATE_ORDER_OPTION_TEXT).click()

    def delete_catalog(self, name):
        catalog_options = self.search_element_by_css(self.ADDITIONAL_OPTIONS_CSS.format(name))
        catalog_options.click()
        self.search_element_by_text('li', self.DELETE_CATALOG_OPTION_TEXT).click()

    def edit_catalog(self, name):
        catalog_options = self.search_element_by_css(self.ADDITIONAL_OPTIONS_CSS.format(name))
        catalog_options.click()
        self.search_element_by_text('li', self.EDIT_CATALOG_OPTION_CSS).click()

    def add_all_products_to_catalog(self, name):
        catalog_options = self.search_element_by_css(self.ADDITIONAL_OPTIONS_CSS.format(name))
        catalog_options.click()
        self.search_element_by_text('li', self.ADD_ALL_PRODUCTS_OPTION_TEXT).click()


