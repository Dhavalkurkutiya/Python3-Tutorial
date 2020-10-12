# pip install wheel
# python setup.py bdist_wheel
# python setup.py sdist bdist_wheel
# pip install package_name
# Import package_name


from setuptools import setup
setup(name="packageharry",
version="0.3",
description="This is code with harry package",
long_description = "This is a very very long description",
author="Harry",
packages=['packageharry'],
install_requires=[])


class Achha:
    def __init__(self):
        print("Constructor ban gaya")

    def achhafunc(self, number):
        print("This is a function")
        return number


