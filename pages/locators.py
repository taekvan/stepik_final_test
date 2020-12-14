from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.ID, "login_form")
	REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    CORRECT_BOOK_IS_ADDED = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_LINK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
    NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    BASKET_VALUE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

