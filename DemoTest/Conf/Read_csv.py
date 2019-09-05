import csv


class Read_csv:
    def get_data(file_name):
        # create an empty list to store rows
        rows = []
        # open the CSV file
        data_file = open(file_name, "r")
        # create a CSV Reader from CSV file
        reader = csv.reader(data_file)
        # skip the headers
        next(reader, None)
        # add rows from reader to list
        for row in reader:
            rows.append(row)
        return rows