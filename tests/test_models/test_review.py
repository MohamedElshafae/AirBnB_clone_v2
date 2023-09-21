#!/usr/bin/python3
"""doc doc"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """doc doc"""

    def __init__(self, *args, **kwargs):
        """doc doc"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """doc doc"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """doc doc"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """doc doc"""
        new = self.value()
        self.assertEqual(type(new.text), str)
