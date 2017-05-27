import unittest
from indexpage import IndexPage
from selenium import webdriver
import time



class Xdailtest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url='http://www.xdaili.cn'


    def test_index(self):
        '''首页所有元素点击测试'''
        index_page=IndexPage(self.driver,self.url,u'讯代理')
        index_page.open()
        index_page.click_free()
        self.driver.back()
        time.sleep(1)
        index_page.click_bran()
        self.driver.back()
        time.sleep(1)
        index_page.click_pri()
        time.sleep(4)
        self.driver.back()



    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)