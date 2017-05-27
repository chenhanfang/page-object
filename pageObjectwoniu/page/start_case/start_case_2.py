import unittest
from pageObjectwoniu.page.function.function_2 import search

class case_1(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        search()
        print('产品介绍测试完了')

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()