#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='iot-demo-webapp',
    version='1.2.112',
    description='Simple webapp for demo purposes.',
    py_modules=['iot-demo-webapp'],
    install_requires=['Flask==1.1.2'],
    include_package_data=True,
    package_data = {'': ['LICENSE']}
)
