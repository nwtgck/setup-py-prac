# (from: https://github.com/masaponto/Python-MLP/blob/master/setup.py)
from distutils.core import setup

setup(
    name='nwtgck_hello',
    version='0.1.0',
    description='setup.py practice',
    author='Ryo Ota',
    author_email='nwtgck@gmail.com',
    install_requires=['scikit-learn', 'numpy'],
    py_modules=["nwtgck_hello"],
    package_dir={'': 'src'}
)