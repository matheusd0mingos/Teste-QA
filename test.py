from page_objects import *
from page_objects import Login_page
from page_objects import Market_page
from page_objects import Check_out_information_page
from page_objects import Cart_page
from page_objects import Finish_page
options = webdriver.ChromeOptions()

driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://www.saucedemo.com/')

login_page=Login_page(driver, 'standard_user')
login_page.login()

market_page=Market_page(driver)
market_page.order()
market_page.add_cart('add-to-cart-test.allthethings()-t-shirt-(red)')
market_page.add_cart('add-to-cart-sauce-labs-onesie')
market_page.enter_cart_page()

cart=Cart_page(driver)
cart.check_out()

check_out=Check_out_information_page(driver)
check_out.go_on()

final=Finish_page(driver)
final.finish()
