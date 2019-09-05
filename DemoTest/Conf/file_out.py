#!/usr/bin/python3
# coding=utf-8
# Filename: file_out.py
import csv
def out_data(info_url, info):
    with open(info_url, 'w', newline='') as t_file:
        csv_writer = csv.writer(t_file)
        for l in info:
            csv_writer.writerow(l)
