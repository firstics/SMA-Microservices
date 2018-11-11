# # Assign Cashier a Job Testcase
# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

# # Find Path to run Google Chrome for Test
# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# BASE_DIR = os.getcwd()
# driver_path = os.path.join(BASE_DIR,"chromedriver")

# # Selenium Run Chrome Driver
# selenium = webdriver.Chrome(executable_path= driver_path,  chrome_options=options)

# # Redirect to login page
# selenium.get('http://127.0.0.1:8000/srd_web/signin')
# time.sleep(1)
# assert 'srd_web/signin' in selenium.current_url

# # Find Elements to Login
# username = selenium.find_element_by_id('username')
# password = selenium.find_element_by_id('password')
# submit = selenium.find_element_by_id('submit') 

# # Fill them to fields
# username.send_keys('hello')
# password.send_keys('123456')
# submit.click()

# # Redirect to monitor page
# selenium.get('http://127.0.0.1:8000/srd_web/index/2018-11-02')
# time.sleep(1)
# assert 'srd_web/index' in selenium.current_url

# # Find nav-assign elements to redirect to assign page
# nav_assign = selenium.find_element_by_id('nav-assign')
# nav_assign.click()
# time.sleep(1)
# assert 'srd_web/assign' in selenium.current_url 

# # Select cashier in dropdown menu
# dropdown = Select(selenium.find_element_by_class_name('f-1'))
# dropdown.select_by_visible_text("pop pongkul")
# submit = selenium.find_element_by_id('submit')
# submit.click()

# # Redirect to monitor page
# nav_assign = selenium.find_element_by_id('nav-index')
# nav_assign.click()

# # Check the record has been changed and same name cahier 
# cashier_name = selenium.find_element_by_id('cashier3')
# assert cashier_name.text == "pop pongkul"

# # Close window
# selenium.close()
# selenium.quit()