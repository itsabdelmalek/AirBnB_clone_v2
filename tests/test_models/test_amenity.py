#!/usr/bin/python3
"""Defines unnittests for models/amenity.py"""
import os
import MySQLdb
import unittest
from datetime import datetime
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


class test_Amenity(test_basemodel):
    """Unittests for testing the Amenity class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
