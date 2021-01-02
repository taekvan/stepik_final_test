from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():



    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"   
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()          # выполняем метод страницы — переходим на страницу логина

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.no_produt_in_basket(link)
        page.basket_is_empty_text_exist()








#def test_guest_should_see_login_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_form()

#def test_guest_should_see_register_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_register_form()
