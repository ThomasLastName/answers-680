
### ~~~
## ~~~ From https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
### ~~~ 

from setuptools import setup, find_packages

setup(
    name = 'package_name',
    version = '1.2.0',
    url = 'https://github.com/ThomasLastName/slug',
    author = 'Thomas Winckelman',
    author_email = 'winckelman@tamu.edu',
    description = 'Description of my package',
    packages = find_packages(),    
    install_requires = ["pyreadr"]    # ~~~ when you pip install `package_name`, pip will also install `pyreadr`
)
