#coding=utf-8
import unittest
from loginpage import LoginPage
from selenium import webdriver
import time

class Caselogin126mail(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = 'http://mail.163.com'
        self.username='chfan1028'
        self.password='777chf10287'

    def test_login_mail(self):
        login_page = LoginPage(self.driver,self.url,u'网易')
        login_page.open()
        login_page.switch_frame('x-URS-iframe')####用户名和密码输入框元素嵌套在这个iframe中了
        login_page.input_username(self.username)
        login_page.input_password(self.password)
        time.sleep(5)
        login_page.click_submit()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

