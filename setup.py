#!/usr/bin/env python
'''
Installer script for the bard module.
'''

from distutils.core import setup

setup (
    name = "bard",
    version = "0.2",
    author = 'Zach Denton',
    author_email = 'zacharydenton@gmail.com',
    url = 'http://zacharydenton.com/',
    description = "A module which generates pseudorandom text. Inspired by the Bard from Asimov's 'Someday'.",
    py_modules = ['bard']
)
