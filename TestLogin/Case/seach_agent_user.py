
import unittest
from selenium import webdriver
from ddt import ddt, data, unpack

from Code import login, test_agent_user_search
from Conf.Read_csv import Read_csv
from Conf.TestReport import TestReport
@ddt
class Seach(unittest.TestCase):
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

    def test_search_01(self):
        data = Read_csv.get_data('D:\Idea_coad\Demo_Test\Data\login_test.csv')
        print(data[0][0])
        login.login_test(self, self.driver, "C0006", "lvliwen", "111111")
        test_agent_user_search.test_agent_user_search(self, self.driver)


if __name__ == '__main__':
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Seach("test_search_01"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #TestReport.Test_report(unittest.TestLoader().loadTestsFromTestCase(Login))
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Seach)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    # suites = unittest.TestSuite()
    # suites.addTests([suite1])
    # TestReport.Test_report(suites)