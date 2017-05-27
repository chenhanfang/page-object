from pageObjectwoniu.log import Logger
from pageObjectwoniu.page.config.config_1 import locat_config


class UIHandle():
    logger = Logger()

    @classmethod
    def __init__(cls,driver):
        cls.driver = driver

    @classmethod
    def get(cls,url):
        cls.logger.loginfo(url)
        cls.driver.get(url)

    @classmethod
    def quit(cls):
        cls.driver.quit()

    @classmethod
    def element(cls,page,element):
        cls.logger.loginfo(page)
        el = cls.driver.find_element(*locat_config[page][element])
        return el

    @classmethod
    def Input(cls,page,element,msg):
        el=cls.element(page,element)
        el.send_keys(msg)

    @classmethod
    def Click(cls,page,element):
        el=cls.element(page,element)
        el.click()