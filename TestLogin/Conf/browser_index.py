from selenium import webdriver

from Code import login
from Conf import file_out

info_url = "E://auto_data/test.csv"
#第一次使用Chrome() 新建浏览器会话
driver = webdriver.Chrome()
# 记录 executor_url 和 session_id 以便复用session
executor_url = driver.command_executor._url
session_id = driver.session_id
login.login_test(driver)      #登录
info_data = [(executor_url, session_id)]
file_out.out_data(info_url, info_data)  #将网页信息保存到文件
