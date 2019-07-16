# coding=UTF-8
import unittest
class FirstCase01(unittest.TestCase):

    def setUp(self):
        print("前置条件")

    def tearDown(self):
        print("后置条件")

    def testfirst01(self):
        print("1111")

    def testfirst02(self):
        print("222")

if __name__ == "__main__":
    unittest.main()

