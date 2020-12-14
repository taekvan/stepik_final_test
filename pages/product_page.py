from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import math



class ProductPage(BasePage):
    def add_to_basket(self):

        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()



    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented") 


    def check_correct_book(self, book_name):

        book_item = self.browser.find_element(*ProductPageLocators.CORRECT_BOOK_IS_ADDED)
        consist = book_name in book_item.text
        assert consist, "You ordered  wrong book"


    def product_name(self):
        
        name_link = self.browser.find_element(*ProductPageLocators.NAME)
        name_value = name_link.text
        return name_value


    def product_price(self):
        
        price_link = self.browser.find_element(*ProductPageLocators.PRICE_LINK)
        price_value = price_link.text
        return price_value


    def basket_product_name_should_be_as_product_name(self, product_name_in_product_page, link):
        
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        consist = product_name_in_product_page == product_name_in_basket
        assert consist, f"The name of odered product doesn't match the product in basket on the page {link}"


    def basket_value_sould_be_as_odered_product(self, odered_product_price):
        
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        consist = odered_product_price in basket_value
        assert consist, "The price of odered product doesn't match the basket value"

    def should_be_basket_button(self, link):
        
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), f"Basket button is not presented on the page {link}"

    def should_be_price(self):
        
        assert self.is_element_present(*ProductPageLocators.PRICE_LINK), "Product price is not presented"



        