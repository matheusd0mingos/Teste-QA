from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import selenium.common.exceptions
from threading import Thread 
import time

#from dependencias import dependencias_install
options = webdriver.ChromeOptions()

default_time=0.4
class Login_page():
    def __init__(self, driver, user, password="secret_sauce") -> None:
        self.user=user
        self.password=password
        self.driver=driver
    
    def login(self):
        username_space = self.driver.find_elements_by_id("user-name") 
        password_space=self.driver.find_elements_by_id("password")
        username_space[0].send_keys(self.user)
        password_space[0].send_keys(self.password)
        login_button=self.driver.find_elements_by_id("login-button")
        login_button[0].click()
        time.sleep(default_time)

class Market_page():
    def __init__(self, driver):
        self.driver=driver

    def order(self):
        order_element=self.driver.find_element_by_xpath("//select[@class='product_sort_container']")
        ddelement=Select(order_element)
        ddelement.select_by_visible_text('Price (low to high)')
        time.sleep(default_time)

    def add_cart(self, item):
        add_cart_button= self.driver.find_element_by_id(item)
        add_cart_button.click()
        time.sleep(default_time)

    def enter_cart_page(self):
        button=self.driver.find_element_by_xpath("//span[@class='shopping_cart_badge']")
        button.click()
        time.sleep(default_time)

class Cart_page():
    def __init__(self, driver) -> None:
        self.driver=driver

    def check_out(self):
        check_out_button=self.driver.find_elements_by_id("checkout")
        check_out_button[0].click()
        time.sleep(default_time)

class Check_out_information_page():
    def __init__(self, driver, first_name='test', last_name='test', zip='test') -> None:
        self.first_name=first_name
        self.last_name=last_name
        self.zip=zip
        self.driver=driver
    
    def go_on(self):
        first_name_space = self.driver.find_elements_by_id("first-name") 
        last_name_space=self.driver.find_elements_by_id('last-name')
        zip_space=self.driver.find_elements_by_id('postal-code')

        first_name_space[0].send_keys(self.first_name)
        last_name_space[0].send_keys(self.last_name)
        zip_space[0].send_keys(self.zip)

        button=self.driver.find_elements_by_id('continue')
        button[0].click()
        time.sleep(default_time)

class Finish_page():
    def __init__(self, driver) -> None:
        self.driver=driver
    
    def finish(self):
        finish_button=self.driver.find_elements_by_id('finish')
        finish_button[0].click()
        time.sleep(3)