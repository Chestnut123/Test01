import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
from Code import login
from Conf.Read_csv import Read_csv
from Conf.TestReport import TestReport
@ddt
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)
    def cleanup(self):
        pass
    #-------------------------------------------------------------------------
    @data(*Read_csv.get_data('D:\\idea-workspace\\PythonTest\\DemoTest\\Data\\login_test.csv'))
    @unpack
    def test_login(self, code, name, pwd):
        login.login_test(self, self.driver, code, name, pwd)


    #参数化
    def test_login_01(self):
        data = Read_csv.get_data('D:\\idea-workspace\\PythonTest\\DemoTest\\Data\\login_test.csv')
        print(data[0][0])
        login.login_test(self, self.driver, data[0][0], data[0][1], data[0][2])


    #跳过测试用例
    @unittest.skip('跳过')
    def test_login02(self):
        login.login_test(self, self.driver, "hjhy ", "lizhenghong", "111111")

if __name__ == '__main__':
    #只加载一个Class
    #TestReport.Test_report(unittest.TestLoader().loadTestsFromTestCase(Login))
    #可以同时加载多个Class
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Login)
    suites = unittest.TestSuite()
    suites.addTests([suite1])
    TestReport.Test_report(suites)