
### ~~~
## ~~~ From https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
### ~~~ 

from setuptools import setup, find_packages

#
# ~~ Load the a .txt file, into a list of strings (each line is a string in the list)
def txt_to_list(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f]

setup(
    name = 'answers_680',
    version = '1.1.0',
    url = 'https://github.com/ThomasLastName/answers-680',
    author = 'Thomas Winckelman',
    author_email = 'winckelman@tamu.edu',
    description = 'Answers to the exercises in labs_680 with improved package structure',
    packages = find_packages(),
    install_requires = txt_to_list("requirements.txt"),
    include_package_data = True,    # ~~~ include certain files other than `.py` files
    package_data={"answers_680": ["*.npy"]}    # ~~~ speicifically, include `.npy` files in the folder "answers_680"
)
