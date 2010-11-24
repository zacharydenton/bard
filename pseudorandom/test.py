#!/usr/bin/env python
import unittest
import doctest

import detokenizers; from detokenizers.tests import *
import generators; from generators.tests import *

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(detokenizers))
    return tests

if __name__ == "__main__":
    unittest.main()
