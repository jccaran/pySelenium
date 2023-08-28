import pytest
import json
from pages.hudl_base import HudlBase
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage


def open_json(testfile):
    try:
        with open(testfile) as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print("File not found. Please create testdata.json file using the testdata.json.sample as a guide.")
        return None


class TestLogin(BaseTest):

    @pytest.mark.sanity()
    @pytest.mark.web()
    def test_hudl_to_login(self):
        test_page = HudlBase(self.driver)
        test_page.open('')
        test_page.login_hudl_from_homepage()
        test_page = LoginPage(self.driver)  # Should be on LoginPage now
        assert test_page.is_loaded()

    @pytest.mark.web()
    def test_login_valid_user(self):
        test_page = HudlBase(self.driver)
        test_page.open('')
        test_page.login_hudl_from_homepage()
        test_page = LoginPage(self.driver)
        user = open_json('testdata.json')
        test_page.login(user["email"], user["password"])
        test_page = HomePage(self.driver)
        assert test_page.is_loaded()

    @pytest.mark.web()
    def test_login_invalid_user(self):
        test_page = HudlBase(self.driver)
        test_page.open('')
        test_page.login_hudl_from_homepage()
        test_page = LoginPage(self.driver)
        test_page.login("johnthephisherman@fakeemail.edu", "nefarious")
        assert test_page.invalid_auth() == "We don't recognize that email and/or password"

    @pytest.mark.web()
    def test_password_masking(self):
        test_page = HudlBase(self.driver)
        test_page.open('')
        test_page.login_hudl_from_homepage()
        test_page = LoginPage(self.driver)
        test_page.enter_email("notimportant@email.edu")
        test_page.enter_password("password")
        assert test_page.password_is_masked("password")

    @pytest.mark.web()
    def test_login_empty_user(self):
        test_page = HudlBase(self.driver)
        test_page.open('')
        test_page.login_hudl_from_homepage()
        test_page = LoginPage(self.driver)
        test_page.login("", "nefarious")
        assert test_page.invalid_auth() == "Please fill in all of the required fields"

    @pytest.mark.web()
    def test_login_empty_password(self):
        test_page = HudlBase(self.driver)
        test_page.open('')
        test_page.login_hudl_from_homepage()
        test_page = LoginPage(self.driver)
        test_page.login("notrealuser@someplacefake.edu", "")
        assert test_page.invalid_auth() == "Please fill in all of the required fields"
