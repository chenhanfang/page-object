from time import sleep

from apppageObject.constant_1 import INDEX_URL
from apppageObject.encapsulation import UIHandle
from apppageObject.page.config.config_1 import browser_config
from apppageObject.desired_caps import desired_caps

def search():
    # desired_caps = {}  # 声明一个appium服务的设置集合
    # desired_caps['platformName'] = 'Android'  # 指定安卓
    # desired_caps['platformVersion'] = '4.4.2'  # 安卓版本
    # desired_caps['deviceName'] = '127.0.0.1:62001'  # 手机的ip可以用adb devices查询到
    # desired_caps['appPackage'] = 'com.tencent.mm'
    # desired_caps['appActivity'] = '.ui.LauncherUI'  # 包的activity属性，appium1.4以上可以直接获取到，其他可以用抓log大法查到，具体查看我博客其他文章
    # desired_caps["unicodeKeyboard"] = "True"
    driver = browser_config['remote'](INDEX_URL,desired_caps)
    uihandle = UIHandle(driver)
    # uihandle.get(INDEX_URL,desired_caps)
    sleep(10)
    # uihandle.Click('微信首页','搜索')
    # driver.get_screenshot_as_file('E:\\pageobject\\apppageObject\\screenshot\\sousuo.jpg')
    # sleep(5)
    # uihandle.Click('微信首页','搜索返回')
    # sleep(3)
    # uihandle.Click('微信首页', '更多')
    uihandle.Click('微信首页','第二个')
    sleep(3)
    # uihandle.Click('微信首页','表情')
    # sleep(1)
    # uihandle.Click('微信首页','表情4')
    uihandle.Click('微信首页','输入框')
    sleep(1)
    uihandle.Input('微信首页','输入框','测试啊哈哈')
    sleep(1)
    uihandle.Click('微信首页','发送')
    sleep(3)


    uihandle.quit()