from selenium.webdriver.common.by import By
from basepage import BasePage

class IndexPage(BasePage):
    freeproxy_loc =(By.XPATH,'html/body/div[1]/div/div[2]/div[2]/a')
    branches_loc = (By.XPATH,'html/body/div[1]/div/div[2]/div[3]/a')
    priceproxy_loc = (By.XPATH,'html/body/div[1]/div/div[2]/div[4]/a')

    def open(self):
        self._open(self.base_url,self.pagetitle)

    def click_free(self):
        self.find_element(*self.freeproxy_loc).click()

    def click_bran(self):
        self.find_element(*self.branches_loc).click()

    def click_pri(self):
        self.find_element(*self.priceproxy_loc).click()

