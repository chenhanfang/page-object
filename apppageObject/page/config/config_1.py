from appium import webdriver


browser_config ={
    'remote':webdriver.Remote,


}
####对appuim的元素定位不是很熟悉，目前只提供id,name,accessibility,xpath,classname
locat_config ={
    '微信首页':{
        '搜索': ['Accessibility',u'搜索'],
        '搜索返回': ['id', 'com.tencent.mm:id/go'],
        '更多':['id','com.tencent.mm:id/f_'],
    },


}