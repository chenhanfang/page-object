from apppageObject.log import Logger
from apppageObject.page.config.config_1 import locat_config
from appium import webdriver
class UIHandle():
    logger=Logger()
    def __init__(self,driver):
        self.driver = driver


    def get(self,url,desired_caps):
        self.driver(url,desired_caps)

    def quit(self):##退出浏览器
        self.driver.quit()

    def element(self,page,element):##查找元素封装
        self.logger.loginfo(page)
        self.driver.implicitly_wait(10)
        type = locat_config[page][element][0]
        yuansu = locat_config[page][element][1]
        if type == 'id':
            el = self.driver.find_element_by_id(yuansu)
        elif type == 'Accessibility':
            el = self.driver.find_element_by_accessibility_id(yuansu)
        elif type == 'name':
            el = self.driver.find_element_by_name(yuansu)
        elif type == 'classname':
            el =self.driver.find_element_by_class_name(yuansu)
        else:
            el = self.driver.find_element_by_xpath(yuansu)
        return el

    def Input(self,page,element,msg):###输入操作封装
        el=self.element(page,element)
        el.clear()
        el.send_keys(msg)

    def Text(self,page,element):##获取元素text封装
        el=self.element(page,element)
        text = el.text
        return text

    def Click(self,page,element):###点击操作封装
        el=self.element(page,element)
        el.click()


