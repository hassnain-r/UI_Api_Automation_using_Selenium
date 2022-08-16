"""Application Login Page"""
from burq_ui.pagees.base_page import BasePage
from resources.constants import *


class Login(BasePage):
    """
    Class for handling Login Page
    """

    def email_id_field(self):
        """
        get email if field
        :return: (WebElement) email field
        """
        return self.wait_and_get_element(self.elements.USER_NAME_CSS)

    def password_field(self):
        """
        get password field
        :return: (WebElement) password field
        """
        return self.wait_and_get_element(self.elements.PASSWORD_CSS)

    def get_login_button(self):
        """
        check for continue button
        :return: (WebElement) continue button
        """
        return self.wait_and_get_element(self.elements.LOGIN_BUTTON_CSS)

    def validate_error_message(self):
        """
        check error message must appear
        :return:(bool) True if error message appears
        """
        return self.compare_actual_and_expected_result(self.elements.ERROR_MESSAGE, error_message)

    def verify_dashboard_is_loaded(self, value_to_match=create_delivery):
        """
        check create delivery button exist
        :return: (bool) True if value matched
        """
        return self.compare_actual_and_expected_result(self.elements.DASHBOARD_TITLE_CSS, value_to_match)

    def login(self, user_name, password):
        self.email_id_field().send_keys(user_name)
        self.password_field().send_keys(password)
        self.get_login_button().click()
