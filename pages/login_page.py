from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        a = "login" in str(self.browser.current_url)
        assert a, "This s not a login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
    
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_REGISTER_BUTTON).click()