from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	LOGIN_FORM = (By.ID, "login_form")
	REGISTRATION_FORM = (By.ID, "register_form")
	REGISTRATION_FORM_EMAIL = (By.ID, "id_registration-email")
	REGISTRATION_FORM_PASSWORD = (By.ID, "id_registration-password1")
	REGISTRATION_FORM_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
	REGISTRATION_FORM_REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
	#register_form > button
	

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    CORRECT_BOOK_IS_ADDED = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_LINK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
    NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    BASKET_VALUE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    DISSAPPEAR_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasetPageLocators():
    BASKET_EMPT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_EXIST_PRODUT = (By.CSS_SELECTOR, "col-sm-6.h3")
  
