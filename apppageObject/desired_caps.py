desired_caps = {}  # 声明一个appium服务的设置集合
desired_caps['platformName'] = 'Android'  # 指定安卓
desired_caps['platformVersion'] = '4.4.2'  # 安卓版本
desired_caps['deviceName'] = '127.0.0.1:62001'  # 手机的ip可以用adb devices查询到
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'  # 包的activity属性，appium1.4以上可以直接获取到，其他可以用抓log大法查到，具体查看我博客其他文章
desired_caps["unicodeKeyboard"] = "True"