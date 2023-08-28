from pages.base_page import BasePage
from utils.locators import HudlBaseLocators


class HudlBase(BasePage):
    def __init__(self, driver):
        super(HudlBase, self).__init__(driver)  # Python2 version

    def expand_login_menu(self):
        self.wait_element(*HudlBaseLocators.LOGIN_SELECT)
        self.driver.find_element(*HudlBaseLocators.LOGIN_SELECT).click()

    def login_hudl(self):
        # The API redirects to https://identity.hudl.com/login?state=<some state value>
        # I don't love this
        # I'd prefer to use the API to find a state value and open additional login tests directly there.
        # Each test going through the base login flow from the homepage seems wasteful and inefficient.
        self.wait_element(*HudlBaseLocators.LOGIN_ICON)
        self.driver.find_element(*HudlBaseLocators.LOGIN_ICON).click()

    def login_hudl_from_homepage(self):
        self.expand_login_menu()
        self.login_hudl()
        return self.driver.current_url
