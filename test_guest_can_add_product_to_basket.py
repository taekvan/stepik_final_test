import pytest
from .pages.product_page import ProductPage
from .pages.product_page import ProductPageLocators
from selenium import webdriver
import time

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
	                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
	                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
	                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
	                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
	                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
	                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",

                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",])


#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_basket_button(link)
    product_name = page.product_name()                        
    product_price = page.product_price()											
    page.add_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.basket_product_name_should_be_as_product_name(product_name, link)
    page.basket_value_sould_be_as_odered_product(product_price)
   
             
