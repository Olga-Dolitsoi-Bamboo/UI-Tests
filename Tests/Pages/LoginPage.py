from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Constants import Data as dt


class Login(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Constants
    EMAIL_URL = 'https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail' \
                '.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser '
    EMAIL_USERNAME_CSS = 'input[type="email"]'
    EMAIL_PASSWORD_CSS = 'input[type="password"]'
    NEXT_BUTTON_CSS = '.qIypjc.TrZEUc.lw1w4b'
    EMAIL_LIST_ID = '#1h'
    FIRST_EMAIL_CSS = f'{EMAIL_LIST_ID}>tr:nth-child(1)'
    LINKED_TEXT_IN_EMAIL = 'Create new password'

    # Locators
    USERNAME_INPUT_NAME = 'login'
    PASSWORD_INPUT_NAME = 'password'
    LOGIN_BUTTON_CSS = 'button[type="submit"]'
    FORGOT_PASSWORD_TEXT = 'Forgot your password?'
    SEND_LINK_BUTTON_CSS = 'button'
    CONFIRM_PASSWORD_NAME = 'confirmPassword'
    EYE_BUTTON_CSS = '.jss70'

    def login_to_portal(self, username, password):
        self.input_in_search_field_name(self.USERNAME_INPUT_NAME, username)
        self.input_in_search_field_name(self.PASSWORD_INPUT_NAME, password)
        self.click_the_button_css(self.LOGIN_BUTTON_CSS)

    def redirect_to_email(self):
        self.driver.get(self.EMAIL_URL)
        self.input_in_search_field_css(self.EMAIL_USERNAME_CSS, dt.EMAIL_USERNAME)
        self.click_the_button_css(self.NEXT_BUTTON_CSS)
        self.input_in_search_field_css(self.EMAIL_PASSWORD_CSS, dt.EMAIL_PASSWORD)
        self.click_the_button_css(self.NEXT_BUTTON_CSS)
        self.click_the_button_css(self.FIRST_EMAIL_CSS)
        self.follow_linked_text(self.LINKED_TEXT_IN_EMAIL)

    def reset_password(self, username, new_password):
        self.follow_linked_text(self.FORGOT_PASSWORD_TEXT)
        self.input_in_search_field_name(self.USERNAME_INPUT_NAME, username)
        self.click_the_button_css(self.SEND_LINK_BUTTON_CSS)
        self.redirect_to_email()
        self.input_in_search_field_name(self.PASSWORD_INPUT_NAME, new_password)
        self.input_in_search_field_name(self.CONFIRM_PASSWORD_NAME, new_password)
        self.click_the_button_css(self.LOGIN_BUTTON_CSS)

    def check_password(self, password):
        eye_button = self.search_element_by_css(self.EYE_BUTTON_CSS)
        password_field = self.search_element_by_css(self.EMAIL_PASSWORD_CSS)
        self.input_in_search_field_name(self.PASSWORD_INPUT_NAME, password)
        eye_button.click()
        actual_pass = password_field.get_attribute('value')
        return actual_pass == password
