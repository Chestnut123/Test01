import time

from Conf import table_search


def page_turn(self, driver, table, page_length):
    self.driver = driver
    self.page_num = 1
    for self.page_num in range(1, int(page_length[-2].text)+1):
        print("第", self.page_num, "页数据")
        table_rows = table.find_elements_by_tag_name("tr")
        time.sleep(1)
        self.page_num =self.page_num + 1
        #获取表格列数
        table_search.table_search(table_rows, "**李")
        self.driver.find_element_by_link_text("下页").click()
        time.sleep(1)