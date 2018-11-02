# Create your tests here.
from django.test import LiveServerTestCase
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from record.models import *
from record.serializers import *
from random import randint

class LoginTestCase(LiveServerTestCase):
    def setUp(self):
        #self.selenium = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.selenium = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',  chrome_options=options)
        super(LoginTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/srd_web/signin')
        #find the element
        time.sleep(5)
        username = selenium.find_element_by_id('username')
        password = selenium.find_element_by_id('password')
        submit = selenium.find_element_by_id('submit')

        username.send_keys('username10')
        password.send_keys('password')
        submit.click()
        time.sleep(5)
        #check the returned result
        assert 'srd_web/index' in selenium.current_url


class LogoutTestCase(LiveServerTestCase):
    def setUp(self):
        #self.selenium = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.selenium = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',  chrome_options=options)
        super(LogoutTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LogoutTestCase, self).tearDown()

    def login_test(self):
        selenium = self.selenium
        #Login
        selenium.get('http://127.0.0.1:8000/srd_web/signin')
        time.sleep(3)
        username = selenium.find_element_by_id('username')
        password = selenium.find_element_by_id('password')
        submit = selenium.find_element_by_id('submit')
        username.send_keys('username10')
        password.send_keys('password')
        submit.click()
        time.sleep(2)

    def test_register(self):
        selenium = self.selenium
        self.login_test()
        logout = selenium.find_element_by_class_name('nav-link')
        logout.click()
        time.sleep(4)
        assert 'index' not in selenium.current_url

class NavTestCase(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.selenium = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',  chrome_options=options)
        super(NavTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(NavTestCase, self).tearDown()

    def login_test(self):
            selenium = self.selenium
            #Login
            selenium.get('http://127.0.0.1:8000/srd_web/signin')
            time.sleep(3)
            username = selenium.find_element_by_id('username')
            password = selenium.find_element_by_id('password')
            submit = selenium.find_element_by_id('submit')
            username.send_keys('username10')
            password.send_keys('password')
            submit.click()
            time.sleep(2)

    def test_register(self):
        selenium = self.selenium

        #Login
        self.login_test()

        nav_assign = selenium.find_element_by_id('nav-assign')
        time.sleep(2)
        nav_assign.click()
        time.sleep(2)
        assert 'srd_web/assign' in selenium.current_url 
        
        nav_verify = selenium.find_element_by_id('nav-verify')
        time.sleep(2)
        nav_verify.click()
        time.sleep(2)
        assert 'srd_web/verify' in selenium.current_url

        nav_history = selenium.find_element_by_id('nav-history')
        time.sleep(2)
        nav_history.click()
        time.sleep(2)
        assert 'srd_web/history' in selenium.current_url 

class AssignTestCase(LiveServerTestCase):

    def setUp(self):
        self.old_index = 0
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.selenium = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',  chrome_options=options)
        super(AssignTestCase, self).setUp()
        
    def tearDown(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/srd_web/assign')
        time.sleep(2)
        #restore_checkbox = selenium.find_element_by_id('r0c'+str(self.old_index))
        self.checkRadioButton(colum=self.old_index)
        submit = selenium.find_element_by_id('submit')
        submit.click()
        time.sleep(2)
        self.selenium.quit()
        super(AssignTestCase, self).tearDown()
    def login_test(self):
        selenium = self.selenium
        #Login
        selenium.get('http://127.0.0.1:8000/srd_web/signin')
        time.sleep(3)
        username = selenium.find_element_by_id('username')
        password = selenium.find_element_by_id('password')
        submit = selenium.find_element_by_id('submit')
        username.send_keys('username10')
        password.send_keys('password')
        submit.click()
        time.sleep(2)
    
    def checkRadioButton(self,row=0,colum=0):
        checkbox = self.selenium.find_element_by_id('r'+str(row)+'c'+str(colum))
        checkbox.click()
        time.sleep(2)
    def test_register(self):
        selenium = self.selenium
        self.login_test()
        selenium.get('http://127.0.0.1:8000/srd_web/assign')
        time.sleep(2)
        i=0
        while(True):
            try:
                cur_checkbox = selenium.find_element_by_id('r0c'+str(i))
                if (cur_checkbox.is_selected()):
                    self.old_index = i
                i=i+1
            except:
                i=i-1
                break
        test_colum = randint(0,i)
        #target_checkbox = selenium.find_element_by_id('r0c'+str(test_colum))
        self.checkRadioButton(colum=test_colum)
        submit = selenium.find_element_by_id('submit')
        #target_checkbox.click()
        submit.click()
        selenium.get('http://127.0.0.1:8000/srd_web/assign')
        time.sleep(2)
        target_checkbox = selenium.find_element_by_id('r0c'+str(test_colum))
        assert True == (target_checkbox.is_selected())

from django.test import TestCase

class CashierCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username1',
            password='password',
            first_name='demo',
            last_name='test')
        cashier, created = Cashier.objects.update_or_create(user=user)

    def test_user_cashier(self):
        """Cashier that has firstname and lastname are correctly identified"""
        user = User.objects.get(first_name="demo")
        cashier = Cashier.objects.get(user=user)
        self.assertEqual(cashier.user.first_name, 'demo')
        self.assertEqual(cashier.user.last_name, 'test')

class ManagerCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username2',
            password='password',
            first_name='demo_manager',
            last_name='test')
        manager, created = Manager.objects.update_or_create(user=user)

    def test_user_manager(self):
        """Manager that has firstname and lastname are correctly identified"""
        user = User.objects.get(username="username2")
        manager = Manager.objects.get(user=user)
        self.assertEqual(manager.user.first_name, 'demo_manager')
        self.assertEqual(manager.user.last_name, 'test')

class DailyRecordCase(TestCase):
    def setUp(self):
        store = Store(store_name="testshop")
        store.save()
        record = DailyRecord(store=store)
        record.save()
    def test_daily_record(self):
        store = Store.objects.get(store_name="testshop")
        record = DailyRecord.objects.get(store=store)
        self.assertEqual(record.store.store_name, 'testshop')