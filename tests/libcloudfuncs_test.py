'''
Tests for the libcloudfuncs module.
'''

import unittest
from mock import Mock
from saltcloud.libcloudfuncs import libcloud_version

class TestLibCloudFuncs(unittest.TestCase):

    def test_libcloud_version(self):
        # Versions >= 0.11.4 do not raise an error
        libcloud_mock = Mock()
        libcloud_valid_versions = \
            ['0.11.4', '0.11.5', '0.12.0', '0.13.4', '1.2.3']
        for version in libcloud_valid_versions:
            libcloud_mock.__version__ = version
            libcloud_version(libcloud_mock)

        # Versions < 0.11.4 raise an error
        libcloud_invalid_versions = \
            ['0.11.3', '0.11.2', '0.11.0', '0.9.1', '0.2.5', '0.0.0']
        for version in libcloud_invalid_versions:
            libcloud_mock.__version__ = version
            with self.assertRaises(ImportError):
                libcloud_version(libcloud_mock)
