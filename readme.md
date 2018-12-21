## python-mldb

### Introduction
python-mldb is an interface for you to combine machine learning development with SQL database.
You can utilize the advantage of SQL database while develop your machine learning application.

### Install
We currently support Python3 only.

First clone or download this repo by
```commandline
git clone https://github.com/johnnychhsu/python-mldb.git
``` 

Run the following command to install :
```python
python setup.py install
```
Then enter python_mldb : 
```commandline
cd python_mldb
```
Modify the MySQL host, user and password in `config.yaml`.

Then run :
```python
python connection_test.py
```
to check whether the install is OK.

### Trouble shooting
If you encounter MySQL error like
```sql
This command is not allowed
```
This is due to the local infile security issue MySQL address.
This can be solved by running the command in mysqlsh :  
```mysql-sql
SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 'ON';
SHOW GLOBAL VARIABLES LIKE 'local_infile';
```


### Example
We provide ipython notebook for you to quick start using python-mldb.
Please check the following links :
1. [Random Forest Classifier](https://github.com/johnnychhsu/python-mldb/blob/master/Example/RF_model_example.ipynb)
