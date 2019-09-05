#coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUP(self):
        print("start")
    def tearDown(self):
        time.sleep(1)
        print("end")
    def test01(self):
        print("执行测试用例01")
    def test03(self):
        print("执行测试用例01")
    def test02(self):
        print("执行测试用例01")
if __name__=="__main__":
    unittest.main()