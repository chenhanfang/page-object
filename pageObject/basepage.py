#coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self,selenium_driver,base_url,pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle


    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def _open(self,url,pagetitle):#打开页面，并校验链接是否正确加载
        self.driver.get(url)
        self.driver.set_window_size(1400, 1400)
        assert self.on_page(pagetitle),u'打开页面失败 %s'%url

    def open(self):###定义open方法，调用_open进行打开链接
        self._open(self.base_url,self.pagetitle)

    def find_element(self,*loc):##重写元素定位方法
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u'%s 页面中未找到 %s是元素'%(self,loc))

    def switch_frame(self,loc):##重写进入frame框架
        return self.driver.switch_to_frame(loc)

    def script(self,src):###定义script方法，用于执行js脚本，范围执行结果
        self.driver.exexute_script(src)

    def send_keys(self,loc,vaule,clear_first=True,click_first=True):##重写输入
        try:
            loc=getattr(self,'_%s'%loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print(u'%s 页面中未能找到%s元素'%(self,loc))

