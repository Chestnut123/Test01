import time
import unittest
from selenium import webdriver
from ddt import ddt, data, unpack

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
        self.driver.get("https://tkzhushou.mylianzhi.com/eldf-sso/login.htm")
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)
    def cleanup(self):
        pass

    @data(*Read_csv.get_data('D:\\idea-workspace\\PythonTest\\DemoTest\\Data\\login_test.csv'))
    @unpack
    def test_login(self, code, name, pwd):
        company_code =self.driver.find_element_by_id('j_companyCode')
        company_code.clear()
        company_code.send_keys(code)
        username = self.driver.find_element_by_id('j_username')
        username.clear()
        username.send_keys(name)
        password = self.driver.find_element_by_id('j_password')
        password.clear()
        password.send_keys(pwd)
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()
        time.sleep(2)
        try:
            actual = self.driver.find_element_by_xpath('//*[@id="show-shortcut"]/span')
        except:
            print("无法找到元素，可能原因：登录失败，页面为跳转")
        finally:
            self.assertEqual(actual.text, name.capitalize())

    @unittest.skip('跳过')
    def test_login01(self):
        company_code =self.driver.find_element_by_id('j_companyCode')
        company_code.clear()
        company_code.send_keys("   ")
        username = self.driver.find_element_by_id('j_username')
        username.clear()
        username.send_keys("   ")
        password = self.driver.find_element_by_id('j_password')
        password.clear()
        password.send_keys("   ")
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()
        time.sleep(2)
        try:
            actual = self.driver.find_element_by_xpath('//*[@id="show-shortcut"]/span')
        except:
            print("无法找到元素，可能原因：登录失败，页面为跳转")
        finally:
            self.assertEqual(actual.text, "  ")


if __name__ == '__main__':
    #TestReport.Test_report(unittest.TestLoader().loadTestsFromTestCase(Login))
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Login)
    #suite2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    suites = unittest.TestSuite()
    suites.addTests([suite1])
    TestReport.Test_report(suites)