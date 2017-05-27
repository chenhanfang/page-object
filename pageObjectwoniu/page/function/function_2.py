from time import sleep

from pageObjectwoniu.constant_1 import CHANPIN
from pageObjectwoniu.encapsulation import UIHandle
from pageObjectwoniu.page.config.config_2 import browser_config,locat_config


def search():
    driver = browser_config['chrome']()
    uihandle = UIHandle(driver)
    uihandle.get(CHANPIN)
    sleep(3)
    uihandle.Click('产品介绍页','独享动态')
    sleep(3)
    uihandle.Click('产品介绍页','独享秒切')
    sleep(2)
    uihandle.quit()