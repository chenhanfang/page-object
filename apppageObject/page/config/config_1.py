from appium import webdriver


browser_config ={
    'remote':webdriver.Remote,


}
####对appuim的元素定位不是很熟悉，目前只提供id,name,accessibility,xpath,classname
locat_config ={
    '微信首页':{
        '搜索': ['content-desc',u'搜索'],
        '搜索返回': ['resrouce-id', 'com.tencent.mm:id/go'],
        '更多':['resrouce-id','com.tencent.mm:id/f_'],
        '第二个':['xpath','//android.widget.ListView[@index="0"]/android.widget.LinearLayout[@index="9"]'],
        '表情':['content-desc',u'表情'],
        # '表情4':['xpath','//com.tencent.mm.ui.mogic.WxViewPager[@index="0"]/android.widget.GridView[@index="0"]/android.widget.FrameLayout[@index="5"]/com.tencent.mm.ui.MMImageView[index="0"]'],
        '发送':['text',u'发送'],
        '输入框':['resource-id','com.tencent.mm:id/a3a'],


    },


}