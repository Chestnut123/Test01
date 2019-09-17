
def table_search(table_rows, content):
    table_cols = []
    num = len(table_rows)
    print("查询到的数据共有", num-1, "条")
    for data in table_rows:
        str = data.text
        str_list = str.split()
        table_cols.append(str_list)
    data_num = 0
    for cols in table_cols:
        for i in cols:
            if i == content:
                print(i+"\t is appear!")
                data_num = data_num + 1
                break
    print("包含"+content+"的数据共有", data_num, "条")
