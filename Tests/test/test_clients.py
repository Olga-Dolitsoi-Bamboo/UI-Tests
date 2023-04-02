import time

from Tests.Pages.Clients.ClientsPage import Clients
from Tests.Pages.Clients.CreateClientPopup import CreateClient
from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Constants import Data as dt
from Tests.Constants import SearchText as st
from Tests.Constants import ExpectedResults as exp
import pytest


class TestClassClient:
    def test_add_client(self, my_app):
        # Page initialisation
        client_page = Clients(my_app)
        login_page = Login(my_app)
        menu_page = Menu(my_app)

        # Login to portal
        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Clients page
        menu_page.go_to_option(st.CLIENTS_TEXT)
        # Go to create client Popup
        create_client = client_page.go_to_create_clients()
        # Create client with following parameters
        create_client.create_client(dt.CLIENT_NAME_1, dt.EXCHANGE_RATE_1, dt.INTEGRATION_TYPE_1,
                                    dt.COMMERCIAL_STRUCTURE_1, dt.SETTLEMENT_METHOD_1, dt.ACCOUNT_TYPE_1,
                                    dt.INVOICE_FREQUENCY_1)
        # Go to created clients and check results
        client_details = client_page.go_to_client_by_name(dt.CLIENT_NAME_1)
        assert client_details.check_other_attributes(exp.EXPECTED_CLIENT_1_INTEGRATION, exp.EXPECTED_CLIENT_1_STATUS,
                                                     exp.EXPECTED_CLIENT_1_COMMISSION)
        assert client_details.check_commercial_structure(dt.COMMERCIAL_STRUCTURE_1)

    def test_edit_client(self, my_app):
        client_page = Clients(my_app)
        login_page = Login(my_app)
        menu_page = Menu(my_app)

        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Clients page
        menu_page.go_to_option(st.CLIENTS_TEXT)
        # Go to create client Popup
        create_client = client_page.go_to_create_clients()
        # Create client with following parameters
        create_client.create_client(dt.CLIENT_NAME_2, dt.EXCHANGE_RATE_2, dt.INTEGRATION_TYPE_2,
                                    dt.COMMERCIAL_STRUCTURE_2, dt.SETTLEMENT_METHOD_2, dt.ACCOUNT_TYPE_2,
                                    dt.INVOICE_FREQUENCY_2)
        # Go to created clients and check results
        client_details = client_page.go_to_client_by_name(dt.CLIENT_NAME_2)
        # Edit clients info
        edit_client = client_details.go_to_edit_client()
        edit_client.edit_client_options(rate=dt.EXCHANGE_RATE_2_EDIT, settlement=dt.SETTLEMENT_METHOD_2_EDIT)
        # Check if changes applied successfully
        assert client_details.check_other_attributes(exp.EXPECTED_CLIENT_2_INTEGRATION, exp.EXPECTED_CLIENT_2_STATUS,
                                                     exp.EXPECTED_CLIENT_2_COMMISSION)
        assert client_details.check_commercial_structure(dt.COMMERCIAL_STRUCTURE_2)

    def test_negative_create_client(self, my_app):
        client_page = Clients(my_app)
        login_page = Login(my_app)
        menu_page = Menu(my_app)

        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Clients page
        menu_page.go_to_option(st.CLIENTS_TEXT)
        # Go to create client Popup
        create_client = client_page.go_to_create_clients()
        # Create client with incorrect client name, exchange rate and empty integration type
        create_client.edit_client_options(name=dt.CLIENT_NAME_3, rate=dt.EXCHANGE_RATE_3,
                                          structure=dt.COMMERCIAL_STRUCTURE_3,
                                          settlement=dt.SETTLEMENT_METHOD_3, account=dt.ACCOUNT_TYPE_3)
        assert create_client.check_error_message_name(dt.NAME_ERROR_MESSAGE)
        assert create_client.check_error_message_name(dt.INTEGRATION_ERROR_MESSAGE)

    def test_add_clients_account(self, my_app):
        client_page = Clients(my_app)
        login_page = Login(my_app)
        menu_page = Menu(my_app)

        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Clients page
        menu_page.go_to_option(st.CLIENTS_TEXT)
        # Go to create client Popup
        create_client = client_page.go_to_create_clients()
        create_client.fill_basic_client_info(dt.CLIENT_NAME_4, dt.EXCHANGE_RATE_4, dt.INTEGRATION_TYPE_4,
                                             dt.COMMERCIAL_STRUCTURE_4, dt.SETTLEMENT_METHOD_4, dt.ACCOUNT_TYPE_4,
                                             dt.INVOICE_FREQUENCY_4)
        client_details = client_page.go_to_client_by_name(dt.CLIENT_NAME_4)
        time.sleep(3)
        client_details.add_account(dt.ACCOUNT_CURRENCY_4, active=True)
        time.sleep(3)
        assert client_details.find_account_row(dt.ACCOUNT_CURRENCY_4) is 2



