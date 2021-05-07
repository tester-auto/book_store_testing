'''
# Shop: отображение страницы товара

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_id("username")
login.send_keys("larry_jons@ex.com")
password = driver.find_element_by_id("password")
password.send_keys("RDF$162dQ#")
driver.find_element_by_css_selector('#menu-item-40>a').click()
driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]').click()
title = driver.find_element_by_class_name('product_title').text
assert title == "HTML5 Forms"

#Shop: количество товаров в категории

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_id("username")
login.send_keys("larry_jons@ex.com")
password = driver.find_element_by_id("password")
password.send_keys("RDF$162dQ#")
driver.find_element_by_css_selector('#menu-item-40>a').click()
driver.find_element_by_css_selector('.cat-item-19>a').click()
qty_product = len(driver.find_elements_by_class_name("product"))
print("Количество продуктов в категории:", qty_product)

#Shop: сортировка товаров

from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_id("username")
login.send_keys("larry_jons@ex.com")
password = driver.find_element_by_id("password")
password.send_keys("RDF$162dQ#")
driver.find_element_by_css_selector('#menu-item-40>a').click()
option = driver.find_element_by_css_selector("[value='menu_order']")
option_default = option.get_attribute("selected")
print("Выбрана сортировка по умолчанию:", option_default)
sort = driver.find_element_by_class_name("orderby")
select = Select(sort)
select.select_by_value("price-desc")
option = driver.find_element_by_css_selector("[value='price-desc']")
option_default = option.get_attribute("value")
if option_default == "price-desc":
    print("Выбрана сортировка от большего к меньшему")
else:
    print("Иная сортировка")

#Shop: отображение, скидка товара

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
login = driver.find_element_by_id("username")
login.send_keys("larry_jons@ex.com")
password = driver.find_element_by_id("password")
password.send_keys("RDF$162dQ#")
driver.find_element_by_css_selector('#menu-item-40>a').click()
driver.find_element_by_css_selector('[title="Android Quick Start Guide"]').click()
old_price = driver.find_element_by_css_selector("del>span").text
assert "600.00" in old_price
new_price = driver.find_element_by_css_selector("ins>span").text
assert "450.00" in new_price
preview = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[title="Android Quick Start Guide"]')))
preview.click()
close_preview = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'pp_close')))
close_preview.click()

#Shop: проверка цены в корзине

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_css_selector('#menu-item-40>a').click()
driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(2)
qty_item = driver.find_element_by_class_name("cartcontents").text
assert "1" in qty_item
price = driver.find_element_by_css_selector("#wpmenucartli .amount").text
assert "180.00" in price
driver.find_element_by_class_name('wpmenucart-contents').click()
wait = WebDriverWait(driver, 10)
total = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.product-subtotal .woocommerce-Price-amount'), "180.00"))
subtotal = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal .woocommerce-Price-amount'), "180.00"))

#Shop: работа в корзине

import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_css_selector('#menu-item-40>a').click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(2)
driver.find_element_by_css_selector('[data-product_id="180"]').click()
driver.find_element_by_class_name("wpmenucart-contents").click()
time.sleep(2)
driver.find_element_by_css_selector('.product-remove [data-product_id="182"]').click()
driver.find_element_by_css_selector(".woocommerce-message>a").click()
qty = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
qty.clear()
qty.send_keys("3")
driver.find_element_by_css_selector('[name="update_cart"]').click()
qty_check = qty.get_attribute("value")
assert qty_check == "3"
time.sleep(2)
driver.find_element_by_css_selector('[name="apply_coupon"]').click()
message = driver.find_element_by_css_selector(".woocommerce-error>li").text
assert message == "Please enter a coupon code."
'''

#Shop: покупка товара
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_css_selector('#menu-item-40>a').click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(2)
driver.find_element_by_class_name("wpmenucart-contents").click()
wait = WebDriverWait(driver, 10)
checkout_btn = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button')))
checkout_btn.click()
first_name = wait.until(
    EC.visibility_of_element_located((By.ID, 'billing_first_name')))
first_name.send_keys('Larry')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys("Jons")
email = driver.find_element_by_id('billing_email')
email.send_keys("larry_jons@ex.com")
phone = driver.find_element_by_id('billing_phone')
phone.send_keys("+79214561235")
driver.find_element_by_id('s2id_billing_country').click()
country = driver.find_element_by_id('s2id_autogen1_search')
country.send_keys("Russia")
driver.find_element_by_id('select2-result-label-393').click()
address = driver.find_element_by_id('billing_address_1')
address.send_keys('example')
city = driver.find_element_by_id('billing_city')
city.send_keys('Moscow')
state = driver.find_element_by_id('billing_state')
state.send_keys('example')
postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('1010000')
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
option = driver.find_element_by_id('payment_method_cheque')
option.click()
driver.find_element_by_id('place_order').click()
thanks = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
method = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.method>strong'), 'Check Payments'))







