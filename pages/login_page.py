from utils.locators import LoginPageLocators
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)  # Python2 version
        # self.base_url = 'https://identity.hudl.com/login' # This doesn't work because of the redirect
        # override the base URL of BasePage with https://identity.hudl.com/login
        # super(LoginPage, self).__init__(driver, self.base_url)  # Python2 version

    def is_loaded(self):
        self.wait_element(*LoginPageLocators.EMAIL)
        self.wait_element(*LoginPageLocators.PASSWORD)
        self.wait_element(*LoginPageLocators.CONTINUE)
        self.wait_element(*LoginPageLocators.FORGOT_PASSWORD)
        self.wait_element(*LoginPageLocators.CREATE_ACCOUNT)
        self.wait_element(*LoginPageLocators.LOGIN_FACEBOOK)
        self.wait_element(*LoginPageLocators.LOGIN_GOOGLE)
        self.wait_element(*LoginPageLocators.LOGIN_APPLE)
        return True

    def invalid_auth(self):
        self.wait_element(*LoginPageLocators.UNDEF_TEXT)
        time.sleep(5)  # This is a hack until I can get the find_element_text function to work right.
        error_message = self.find_element(*LoginPageLocators.UNDEF_TEXT).text
        return error_message

    def enter_email(self, email):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.EMAIL).send_keys(email)

    def enter_password(self, password):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def password_is_masked(self, password):
        password_field = self.find_element(*LoginPageLocators.PASSWORD)
        return password_field.text != password  # Probably a better way to do this.

    def click_login_button(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.CONTINUE).click()

    def login(self, user, password):
        self.enter_email(user)
        self.enter_password(password)
        self.click_login_button()

    def forgot_password(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.FORGOT_PASSWORD).click()

    def create_account(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.CREATE_ACCOUNT).click()

    def login_facebook(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.LOGIN_FACEBOOK).click()

    def login_google(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.LOGIN_GOOGLE).click()

    def login_apple(self):
        if self.is_loaded():
            self.find_element(*LoginPageLocators.LOGIN_APPLE).click()





