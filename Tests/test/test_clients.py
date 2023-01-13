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
        create_client = CreateClient(my_app)

        # Login to portal
        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Clients page
        menu_page.go_to_option(st.CLIENTS_TEXT)
        # Go to create client Popup
        client_page.go_to_create_clients()
        # Create client with following parameters
        create_client.create_client(dt.CLIENT_NAME_1, dt.EXCHANGE_RATE_1, dt.INTEGRATION_TYPE_1,
                                    dt.COMMRECIAL_STRUCTURE_1, dt.SETTLEMENT_METHOD_1, dt.ACCOUNT_TYPE_1)
        # Go to created clients and check results
        client_details = client_page.go_to_client_by_name(dt.CLIENT_NAME_1)
        time.sleep(15)
        assert client_details.check_other_attributes('Api', 'Active',
                                                     '0 %')
        assert client_details.check_commercial_structure(dt.COMMRECIAL_STRUCTURE_1)
        assert client_details.has_catalog() == False



