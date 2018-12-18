#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:07:13 2018

@author: jeff_lu
"""
import pandas as pd
import numpy as np
from python_mldb.utils import _check_table_not_exist


class Dataset(object):
    def __init__(self, query_handler):
        self.query_handler = query_handler

    def save_to_database(self, csv_file, table_name):
        if not _check_table_not_exist(self.query_handler, table_name):
            print("Warning: Table {} already existed!".format(table_name))
            self.query_handler.flush_cursor()
            return
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
        self.query_handler.flush_cursor()
        self.query_handler.run_query(sql_query)
        load_query = ("LOAD DATA LOCAL INFILE '" + csv_file + "' INTO TABLE "
                      + table_name)
        load_query += (" FIELDS TERMINATED BY ',' ENCLOSED BY '\"' "
                       + "LINES TERMINATED BY '\r\n' IGNORE 1 LINES")
        self.query_handler.run_query(load_query)

    def load_from_database(self, name):
        if _check_table_not_exist(self.query_handler, name):
            print("Warning: Table {} not exists!".format(name))
            self.query_handler.flush_cursor()
            return
        select_query = "SHOW COLUMNS FROM " + name
        self.query_handler.flush_cursor()
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

    def summary(self, name):
        if _check_table_not_exist(self.query_handler, name):
            print("Warning: Table {} not exists!".format(name))
            self.query_handler.flush_cursor()
            return
        select_query = "SHOW COLUMNS FROM " + name
        self.query_handler.flush_cursor()
        self.query_handler.run_query(select_query)
        rows = []
        aggregate_col = []
        data = []
        for item in self.query_handler.cursor:
            rows.append(item[:2])
        for item in rows:
            col_type = item[1].split("(")
            if col_type[0] == "int" or col_type[0] == "float":
                aggregate_col.append(item)
        for item in aggregate_col:
            select_query = ("SELECT AVG(" + item[0] + "), "
                            + "MIN(" + item[0] + "), " + "MAX(" + item[0] + ")"
                            + ", SUM(" + item[0] + ") " + "FROM " + name)
            self.query_handler.run_query(select_query)
            for result in self.query_handler.cursor:
                data.append(result)
        data = np.array(data)
        aggregate_col = np.array(aggregate_col)
        col_name = aggregate_col[:, 0].reshape(-1, 1)
        result = np.hstack((col_name, data))
        columns = ['Column', 'AVG', 'MIN', 'MAX', 'SUM']
        return pd.DataFrame(result, columns=columns)

    def delete_data(self, name):
        if _check_table_not_exist(self.query_handler, name):
            print("Warning: Table {} not exists!".format(name))
            self.query_handler.flush_cursor()
            return
        delete_query = "DROP TABLE {};".format(name)
        self.query_handler.flush_cursor()
        self.query_handler.run_query(delete_query)

    def get_data(self):
        pass
