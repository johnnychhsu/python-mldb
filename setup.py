from setuptools import setup, find_packages

setup(
    name='python-mldb',
    version='0.1',
    packages=find_packages(exclude=['Example']),
    url='',
    license='',
    author='johnnyhsu',
    author_email='',
    description='A SQL application with machine learning in Python3',
    install_requires=[
        'numpy',
        'pandas',
        'mysql-connector-python',
        'scikit-learn',
    ],
)
