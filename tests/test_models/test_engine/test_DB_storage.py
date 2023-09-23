#!/usr/bin/python3
"""unittest for db_storage"""

import unittest
from os import getenv
from models.engine.db_storage import DBStorage

@unittest.skipIf(getenv("HBN_TYPE_STORAGE") != 'db', 
                 "Test is not relevant for DBStorage")
class test_db_storage(unittest.TestCase):
    """doc doc"""

    def test_doc(self):
        """test for DB"""
        self.assertIsNot(DBStorage.__doc__, None)
