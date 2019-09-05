from Conf import input_csv
from Conf.Read_csv import Read_csv
from Conf.ReuseChrome import ReuseChrome
from ddt import ddt, data, unpack
from Conf.TestReport import TestReport
import unittest
import time
@ddt
class Login(unittest.TestCase):

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        info_url = "E://auto_data/test.csv"
        info_data = input_csv.input_data(info_url)  #读取文件中保存的网页信息
        info = info_data[0]
        executor_url = info[0]
        session_id = info[1]
        # 使用ReuseChrome()复用上次的session
        self.driver = ReuseChrome(command_executor=executor_url, session_id=session_id)
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass
    @data(*Read_csv.get_data('D:\\idea-workspace\\untitled\\Data\\login_test.csv'))
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
        self.driver.find_element_by_xpath('//a[@title="登出"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[@id="bot2-Msg1"]').click()
        time.sleep(1)

if __name__ == "__main__":
    #构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(Login("test_login"))
    #执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #TestReport.Test_report(suite)
    TestReport.Test_report(unittest.TestLoader().loadTestsFromTestCase(Login))
