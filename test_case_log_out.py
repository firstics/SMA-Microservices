import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
selenium = webdriver.Chrome(executable_path='/chromedriver',  chrome_options=options)
selenium.get('http://127.0.0.1:8000/srd_web/signin')

username = selenium.find_element_by_id('username')
password = selenium.find_element_by_id('password')
submit = selenium.find_element_by_id('submit')

username.send_keys('hello')
password.send_keys('123456')
submit.click()

time.sleep(1)
#check the returned result
assert 'srd_web/index' in selenium.current_url

logout = selenium.find_element_by_id('nav-logout')
logout.click()
time.sleep(1)
assert 'srd_web/signin' in selenium.current_url

selenium.close()
selenium.quit()