#!/usr/bin/env python
'''
Installer script for the bard module.
'''

from distutils.core import setup
import bard

setup (
    name = "bard",
    description = "A module for natural language generation.",

    author = bard.__author__,
    author_email = bard.__author_email__,
    version = bard.__version__,
    url = bard.__url__,
    long_description = bard.__longdescr__,
    license = bard.__license__,
    classifiers = bard.__classifiers__,
    packages = ['bard',
                'bard.generators',
                'bard.detokenizers',
               ],
    scripts = ['bard-tale'],
    requires = ['nltk']
)
