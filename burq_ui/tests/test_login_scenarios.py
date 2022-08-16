"""Check All Login Test Scenarios"""
from burq_ui.pagees.login_page import Login
import pytest
import logging
from resources.constants import *


@pytest.mark.usefixtures("setup")
class TestLogin:
    user_name = Login.env_values("USER_NAME")
    password = Login.env_values("PASSWORD")

    def test_login_with_valid_credentials(self):
        """
        Go to Browser
        Launch Application
            Login Screen Appears
        Enter Valid username and Password
        Hit Login Button
            Dashboard is loaded successfully BY validating create delivery button located
        """
        main_page = Login(self.driver)
        main_page.login(user_name=self.user_name, password=self.password)
        assert main_page.verify_dashboard_is_loaded()
        logging.info("User is successfully Logged in")

    def test_login_with_invalid_password(self):
        """
        Go to Browser
        Launch Application
            Login Screen Appears
        Enter Valid Email Id and invalid Password
        Hit Login Button
            error message appears and value error value must match with the one we provided
        """
        main_page = Login(self.driver)
        main_page.login(user_name=self.user_name, password=invalid_value)
        assert main_page.validate_error_message()
        logging.info(f"error message appears and value error value must match with: {error_message}")

    def test_login_with_invalid_username(self):
        """
        Go to Browser
        Launch Application
            Login Screen Appears
        Enter inValid username and valid Password
        Hit Login Button
            error message appears and value error value must match with the one we provided
        """
        main_page = Login(self.driver)
        main_page.login(user_name=invalid_value, password=self.password)
        assert main_page.validate_error_message()
        logging.info(f"error message appears and value error value must match with: {error_message}")
