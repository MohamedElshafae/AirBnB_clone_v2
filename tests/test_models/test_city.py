#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """doc doc"""

    def __init__(self, *args, **kwargs):
        """doc doc"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """doc doc"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """doc doc"""
        new = self.value()
        self.assertEqual(type(new.name), str)
