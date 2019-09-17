import unittest
import os
from Conf.TestReport import TestReport
import sys

#用例存放路径
case_path = os.path.join(os.getcwd(), "Case")
#报告存放路径
report_path = os.path.join(os.getcwd(), "Reporter")
code_path = os.path.join(os.getcwd(), "Code")
conf_path = os.path.join(os.getcwd(), "Conf")
data_path = os.path.join(os.getcwd(), "Data")

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="login*.py", top_level_dir=None)
    #print(discover)
    return discover


if __name__ =="__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    TestReport.Test_report(all_case(),sys.argv[1])
