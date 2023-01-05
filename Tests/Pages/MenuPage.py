from Tests.BaseWrapper.Driver import DriverWrapper


class Menu(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    MENU_LIST_CSS = '.jss49'
    ORDERS_TEXT = ['Orders', 'div']
    PRODUCTS_TEXT = ['Products', 'div']
    SUPPLIERS_TEXT = ['Suppliers', 'li']
    FINANCE_TEXT = ['Finance', 'div']
    CLIENTS_TEXT = ['Clients', 'li']
    MARKETPLACES_TEXT = ['Marketplaces', 'div']
    REPORTS_TEXT = ['Reports', 'div']
    ANALYTICS_TEXT = ['Analytics', 'li']
    MENU_OPTION_CSS = 'jss272'
    NEW_ORDER_TEXT = ['New Order', 'li']
    SOPPING_CARTS_TEXT = ['Shopping Carts', 'li']
    ORDER_HISTORY_TEXT = ['Order History', 'li']
    CARDS_HISTORY_TEXT = ['Cards History', 'li']
    BRANDS_TEXT = ['Brands', 'li']
    PRODUCT_LIST_TEXT


    def get_menu_list(self):
        menu_list = self.find_all_elements_by_css(self.MENU_LIST_CSS)
        return menu_list

    def check_menu_list_elements(self):
        list_elements = self.get_menu_list()
        names_list = []
        for element in list_elements:
            names_list.append(element.text)

