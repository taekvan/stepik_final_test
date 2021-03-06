from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

import time
import pytest


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-age-of-the-pussyfoot_89/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "!@#$%qwert") 
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-age-of-the-pussyfoot_89/"
        page = BasketPage(browser, link)
        page.open()
        page.should_be_basket_button(link)
        product_name = page.product_name()                        
        product_price = page.product_price()                                           
        page.add_to_basket()
        page.should_be_basket_product_name(link)
        page.basket_product_name_should_be_as_product_name(product_name, link)
        page.should_be_basket_value(link)
        page.basket_value_should_be_as_odered_product(product_price)




   
        
            

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-age-of-the-pussyfoot_89/"
        page = BasketPage(browser, link)
        page.open()
        page.should_be_basket_button(link)
        product_name = page.product_name()                        
        product_price = page.product_price()                                           
        page.add_to_basket()
        page.should_be_basket_product_name(link)
        page.basket_product_name_should_be_as_product_name(product_name, link)
        page.should_be_basket_value(link)
        page.basket_value_should_be_as_odered_product(product_price)
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-age-of-the-pussyfoot_89/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.no_produt_in_basket(link)
        page.basket_is_empty_text_exist()
  

    



@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_form()
        page.should_be_register_form()
