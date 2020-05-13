#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''


def _requires_from_file(filename):
    return open(filename).read().splitlines()


# version
here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'pytab',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '0.0.dev0')

setup(
    name='pytab',
    version=version,
    url='https://github.com/HiroshiARAKI/pytable',
    author='Hiroshi ARAKI',
    author_email='araki@hirlab.net',
    maintainer='Hiroshi ARAKI',
    maintainer_email='araki@hirlab.net',
    description='pTable is the library to plot table easily!',
    long_description=readme,
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.1.2',
        'pandas>=1.0.3',
        'numpy',
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
)
