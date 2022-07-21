from page_objects import *
options = webdriver.ChromeOptions()

driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://www.saucedemo.com/')

usuario='standard_user'

lista_itens=['add-to-cart-test.allthethings()-t-shirt-(red)', 'add-to-cart-sauce-labs-onesie']

first_name='test'
last_name='test'
zip='test'

login_page=Login_page(driver, usuario)
login_page.login()

market_page=Market_page(driver)
market_page.order()
for item in lista_itens:
    market_page.add_cart(item)
market_page.enter_cart_page()

cart=Cart_page(driver)
cart.check_out()

check_out=Check_out_information_page(driver, first_name, last_name, zip)
check_out.go_on()

final=Finish_page(driver)
final.finish()