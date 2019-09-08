# import os.path
# import sys
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

import unittest

testmodules = [
    'tests.fetch_tests',
    'tests.file_handler_tests',
    'tests.request_handler_tests',
]

suite = unittest.TestSuite()

for t in testmodules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
