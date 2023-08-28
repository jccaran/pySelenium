from utils.locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.locators = HomePageLocators
        super(HomePage, self).__init__(driver)  # Python2 version

    def is_loaded(self):
        self.wait_element(*HomePageLocators.DISPLAY_NAME)
        self.wait_element(*HomePageLocators.DISPLAY_EMAIL)
        if self.get_url() == "https://www.hudl.com/home":
            return True
        else:
            return False

    def get_display_name(self):
        self.wait_element(*HomePageLocators.DISPLAY_NAME)
        return self.find_element(*HomePageLocators.DISPLAY_NAME).text

    def get_display_email(self):
        self.wait_element(*HomePageLocators.DISPLAY_EMAIL)
        return self.find_element(*HomePageLocators.DISPLAY_EMAIL).text