from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver, base_url='https://www.hudl.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 5

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_element_by_data_qa_id(self, data_value):
        locator = (By.CSS_SELECTOR, f"[data-qa-id='{data_value}']")
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def wait_element_text(self, *locator, text):
        try:
            WebDriverWait(self.driver, self.timeout).until(ec.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            print("\n * TEXT ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()
