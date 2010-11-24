#!/usr/bin/env python
import unittest
import doctest

from detokenizers.tests import *
from generators.tests import *

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(detokenizers))
    return tests

if __name__ == "__main__":
    unittest.main()
