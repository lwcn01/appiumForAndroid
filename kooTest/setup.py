#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name="AutoTest",
    version="1.0",
    packages=find_packages(),
    scripts=['Runner.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[ 'xlrd','Appium-Python-Client','selenium','docutils>=0.3'],

    package_data={
        # If any package contains *.xml or *.xlsx files, include them:
        '': ['*.xml', '*.xlsx'],
        # And include any *.bat files found in the 'kooTest' package, too:
        'kooTest': ['*.bat'],
    },

    # metadata for upload to PyPI
    author="NEW",
    author_email="xxxxxx@163.com",
    description="This is an Appium TestFramwork",
    license="PSF",
    keywords="",
    url="http://github.com",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)