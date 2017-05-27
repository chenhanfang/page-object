from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import *

browser_config ={
    'ie':webdriver.Ie,
    'chrome':webdriver.Chrome,

}
locat_config ={
    '讯代理首页':{
        '免费代理': ['xpath','html/body/div[1]/div/div[2]/div[2]/a'],
        '产品介绍': ['xpath', 'html/body/div[1]/div/div[2]/div[3]/a'],
    },
    '产品介绍页':{
            '独享动态':['xpath','.//*[@id="baike"]/div[2]/div[1]/div[2]/span'],
            '独享秒切':['xpath','.//*[@id="baike"]/div[2]/div[1]/div[3]/span'],
        }

}