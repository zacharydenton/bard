#!/usr/bin/env python
'''
Installer script for the pseudorandom module.
'''

from distutils.core import setup

setup (
    name = "pseudorandom",
    version = "0.2",
    author = 'Zach Denton',
    author_email = 'zacharydenton@gmail.com',
    url = 'http://zacharydenton.com/',
    description = "A module which generates pseudorandom text.",
    py_modules = ['pseudorandom']
)
