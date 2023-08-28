import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self):
        # Read config file
        try:
            with open('config.json') as config_file:
                config = json.load(config_file)
        except Exception as e:
            print(f'Something went wrong: {e}')

        # Set up Browser options and initialize driver
        if config['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            if config['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            try:
                self.driver = webdriver.Chrome(options=options)
            except Exception as e:
                print(f'Something went wrong: {e}')
        elif config['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            if config['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            try:
                self.driver = webdriver.Firefox(options=options)
            except Exception as e:
                print(f'Something went wrong: {e}')
        else:
            raise Exception("Unsupported or Invalid Browser")

        self.driver.implicitly_wait(5)
        # Return driver
        yield
        # Teardown
        self.driver.close()
        self.driver.quit()

