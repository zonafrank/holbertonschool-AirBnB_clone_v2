#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.args = {
            "name": '',
            "state_id": ''
        }

    def test_state_id(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value(**self.args)
        self.assertEqual(type(new.name), str)
