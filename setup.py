#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='spark2aks',
    version='1.0.0',
    description='Pyspark on AKS test project',
    packages=['src',],
    install_requires=['pyspark', ],
    zip_safe=False
)