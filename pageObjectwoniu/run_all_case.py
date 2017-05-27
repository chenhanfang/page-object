#coding=utf-8
from HTMLTestRunner  import HTMLTestRunner
import time
import unittest



if __name__ =='__main__':
    testunit=unittest.TestSuite()
    now = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
    filename = "result\\"+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner (stream=fp,
                           title= '讯代理测试',
                           description= '用例执行情况：')
    discover=unittest.defaultTestLoader.discover('E:\\test2\\pageObjectwoniu\\page\\start_case',pattern='start_case*.py')
    runner.run(discover)
    fp.close()