### python-mldb

#### Introduction
python-mldb is an interface for you to combine machine learning development with SQL database.
You can utilize the advantage of SQL database while develop your machine learning application.

#### Install
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

#### Example
We provide ipython notebook for you to quick start using python-mldb.
Please check the following links :
1. [Random Forest Classifier](https://github.com/johnnychhsu/python-mldb/blob/master/Example/mldb_example.ipynb)
