import csv
def input_data(info_url):
    file = open(info_url)
    reader = csv.reader(file)
    data = []
    for list in reader:
        data.append(list)
    file.close()
    file.close()
    return data




