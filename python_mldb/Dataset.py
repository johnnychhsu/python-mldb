#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:07:13 2018

@author: jeff_lu
"""
import pandas as pd
import numpy as np


class Dataset(object):
    def __init__(self, query_handler):
        self.query_handler = query_handler

    def save_to_database(self, csv_file, table_name):
        data = pd.read_csv(csv_file, nrows=2)
        col_name = []
        col_type = []
        for name in data.columns:
            col_name.append(name)
            if data[name].dtype == "int64":
                col_type.append("INT")
            elif data[name].dtype == "float64":
                col_type.append("FLOAT")
            else:
                col_type.append("VARCHAR(100)")
        sql_query = "CREATE TABLE " + table_name + " ("
        for i in range(len(col_name)):
            attribute = col_name[i] + " " + col_type[i] + ","
            sql_query += attribute
        sql_query = sql_query[:-1]
        sql_query += ")"
        self.query_handler.run_query(sql_query)
        load_query = "LOAD DATA LOCAL INFILE '" + csv_file + "' INTO TABLE "
        + table_name
        load_query += " FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'"
        + "IGNORE 1 LINES"
        self.query_handler.run_query(load_query)

    def load_from_database(self, name):
        select_query = "SHOW COLUMNS FROM " + name
        self.query_handler.run_query(select_query)
        rows = []
        data = []
        for item in self.query_handler.cursor:
            rows.append(item[0])
        select_query = "SELECT * FROM " + name
        self.query_handler.run_query(select_query)
        for item in self.query_handler.cursor:
            data.append(item)
        data = np.array(data)

        return pd.DataFrame(data, columns=rows)

    def get_data(self):
        pass
