'''
#Registration_login: регистрация аккаунта

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_link_text("My Account").click()
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("larry_jons@ex.com")
reg_pass = driver.find_element_by_id("reg_password")
reg_pass.send_keys("RDF$162dQ#")
driver.find_element_by_css_selector('[name="register"]')

'''
# Registration_login: логин в систему

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
driver.find_element_by_css_selector('[name="login"]').click()
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation>ul>li:nth-child(6) a").text
assert logout == "Logout"