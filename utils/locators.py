from selenium.webdriver.common.by import By


def find_element_by_data_qa_id(data_value):
    locator = (By.CSS_SELECTOR, f"[data-qa-id='{data_value}']")
    return locator


class HudlBaseLocators:
    SITE_LOGO = find_element_by_data_qa_id('site-logo')
    LOGIN_SELECT = find_element_by_data_qa_id('login-select')
    LOGIN_ICON = find_element_by_data_qa_id('login-hudl')
    LOGIN = find_element_by_data_qa_id('login')
    LOGIN_WYSCOUT = find_element_by_data_qa_id('login-wyscout')
    LOGIN_VOLLEYMETRICS = find_element_by_data_qa_id('login-volleymetrics')
    LOGIN_WIMU_CLOUD = find_element_by_data_qa_id('login-wimu')


class LoginPageLocators:
    UNDEF_TEXT = find_element_by_data_qa_id('undefined-text')
    EMAIL_REQUIRED = (By.ID, 'uniName-947Help')
    HELP_MESSAGE = find_element_by_data_qa_id('undefined-help-text')
    USER_HELP = find_element_by_data_qa_id('useraccount-help-text')
    REQUIRED = find_element_by_data_qa_id('undefined-help-text')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    CONTINUE = (By.ID, 'logIn')
    FORGOT_PASSWORD = (By.ID, 'forgot-password')
    LOGIN_FACEBOOK = (By.ID, 'btn-facebook')
    LOGIN_GOOGLE = (By.ID, 'btn-google')
    LOGIN_APPLE = (By.ID, 'btn-apple')
    CREATE_ACCOUNT = (By.ID, 'btn-show-signup')


class HomePageLocators:
    DISPLAY_NAME = (By.CLASS_NAME, 'hui-globaluseritem__display-name')
    DISPLAY_EMAIL = (By.CLASS_NAME, 'hui-globaluseritem__email')