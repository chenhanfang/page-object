from time import sleep

from pageObjectwoniu.constant_1 import INDEX_URL
from pageObjectwoniu.encapsulation import UIHandle
from pageObjectwoniu.page.config.config_1 import browser_config


def search():
    driver = browser_config['chrome']()
    uihandle = UIHandle(driver)
    uihandle.get(INDEX_URL)
    sleep(3)
    uihandle.Click('讯代理首页','免费代理')
    sleep(3)
    uihandle.Click('讯代理首页','产品介绍')
    sleep(3)
    uihandle.quit()