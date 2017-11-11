# (from: https://github.com/masaponto/Python-MLP/blob/master/setup.py)
# (from: https://qiita.com/masashi127/items/5bfcba5cad8e82958844)

from setuptools import setup, find_packages

import sys

sys.path.append('./src')
sys.path.append('./tests')

setup(
    name='nwtgck_hello',
    version='0.1.0',
    description='setup.py practice',
    author='Ryo Ota',
    author_email='nwtgck@gmail.com',
    install_requires=['scikit-learn', 'numpy', 'SciPy'],
    py_modules=["nwtgck_hello"],
    packages=find_packages(),
    test_suite='nwtgck_hello_test.suite'
)