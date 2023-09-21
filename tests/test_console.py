#!/usr/bin/python3
"""unittest for console"""

import unittest
import console


class test_console(unittest.TestCase):
    """test console"""

    def test_doc_console(self):
        """test for documentation"""
        self.assertIsNot(console.__doc__, None)
