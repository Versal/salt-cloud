'''
Tests for the saltcloud.utils.parsers module.
'''

import unittest
from saltcloud.utils.parsers import SaltCloudParser

class TestParsers(unittest.TestCase):
    
    def test_query_arg(self):
        parser = SaltCloudParser()
        parser.parse_args(args=[])
        self.assertFalse(parser.options.query)

        parser.parse_args(args=['-Q'])
        self.assertTrue(parser.options.query)
