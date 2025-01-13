
### ~~~
## ~~~ From https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
### ~~~ 

from setuptools import setup, find_packages

setup(
    name = 'answers_680',
    version = '1.0.0',
    url = 'https://github.com/ThomasLastName/answers-680',
    author = 'Thomas Winckelman',
    author_email = 'winckelman@tamu.edu',
    description = 'Answers to the exercises in labs_680 with improved package structure',
    packages = find_packages(),
    include_package_data = True # ~~~ include the `.npy` file
)
