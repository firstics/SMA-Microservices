# Assign Cashier a Job
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
selenium = webdriver.Chrome(executable_path='/Users/atichatlappanopakron/Downloads/chromedriver',  chrome_options=options)
selenium.get('http://127.0.0.1:8000/srd_web/index/2018-11-02')

nav_assign = selenium.find_element_by_id('nav-assign')
nav_assign.click()
assert 'srd_web/assign' in selenium.current_url 

dropdown = Select(selenium.find_element_by_class_name('f-1'))
dropdown.select_by_visible_text("pop pongkul")
submit = selenium.find_element_by_id('submit')
submit.click()

nav_assign = selenium.find_element_by_id('nav-index')
nav_assign.click()

cashier_name = selenium.find_element_by_id('cashier3')
assert cashier_name.text == "pop pongkul"

selenium.close()
selenium.quit()