from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_email_page(self):
        self.should_be_login_form()
        self.should_be_login_email_field()
        self.should_be_login_password_field()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login from is not be present"

    def should_be_login_email_field(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "login email field is not be present"

    def should_be_login_password_field(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "login password field is not be present"


