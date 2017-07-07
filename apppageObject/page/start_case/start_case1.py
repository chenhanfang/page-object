import unittest
from  apppageObject.page.function.function_1 import search


class case_1(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        search()
        print('首页测试完了')

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()