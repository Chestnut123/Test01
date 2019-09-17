
import time
from selenium.webdriver.support.select import Select
from Conf.page_turn import page_turn
def test_agent_user_search(self, driver):
    self.driver = driver
    #用户管理 //*[@id="menu_275"]/a/b/em
    self.driver.find_element_by_xpath("//*[@id='menu_275']/a/b/em").click()
    time.sleep(1)
    #用户管理（子）//*[@id="menu_277"]/a
    self.driver.find_element_by_xpath("//*[@id='menu_277']/a").click()
    time.sleep(1)
    #点击益发特
    self.driver.find_element_by_xpath('//*[@id="agent_tree_1_span"]').click()
    time.sleep(1)
    #点击社区
    self.driver.find_element_by_xpath("//*[@id='householder_search_form']/fieldset/div/section[1]/div/span/span[1]/span").click()
    time.sleep(1)
    #选择社区
    option_click = self.driver.find_element_by_xpath('//*[@id="select2-my_select2-results"]')
    option = option_click.find_elements_by_tag_name("li")
    option[2].click()
    #住户类型
    select_list = self.driver.find_element_by_xpath("//*[@id='householder_search_form']/fieldset/div/section[2]/label[2]/select")
    list_01 = Select(select_list)
    #选择下拉框的值
    list_01.select_by_visible_text("业主")
    #住户状态
    select_list_02 = self.driver.find_element_by_xpath('//*[@id="householder_search_form"]/fieldset/div/section[3]/label[2]/select')
    list_02 = Select(select_list_02)
    list_02.select_by_index(2)
    #查询
    self.driver.find_element_by_xpath("//*[@id='householder_search_form']/footer/div/button[1]").click()
    time.sleep(1)
    #查询表格数据
    table = self.driver.find_element_by_id("user_list_table")
    time.sleep(1)
    #获取表格行数
    table_rows = []
    #table_rows = table.find_elements_by_tag_name("tr")
    #time.sleep(1)
    #获取表格列数

    page_ul = self.driver.find_element_by_xpath('//*[@id="user_list_table_paginate"]/ul')
    page_length = page_ul.find_elements_by_tag_name("li")
    #print(page_length[-2].text)
    page_turn(self, self.driver, table, page_length)

