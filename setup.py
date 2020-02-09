#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from setuptools import setup

with open('installer/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='installer',
    version=version,
    description='Run a series of command',
    author="Ahmadi",
    packages=['installer'],
    python_requires='>=3.6',
    zip_safe=False)
