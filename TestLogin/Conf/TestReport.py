import HTMLTestRunner_cn
import datetime
class TestReport:
    def Test_report(suites, id):
        num = str(id)
        now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-')
        file_path = "Reporter\\"+now_time+num+"result.html"
        file_result = open(file_path, 'wb')
        runer = HTMLTestRunner_cn.HTMLTestRunner(title="测试报告", description="登录测试", stream=file_result, verbosity=2, retry=0 , save_last_try=True)
        runer.run(suites)
