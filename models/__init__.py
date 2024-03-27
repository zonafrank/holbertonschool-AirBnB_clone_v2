#!/usr/bin/python3
"""This module is an interface that switches storage
to instantiates an object of class FileStorage or DBStorage"""
from os import environ


storage_type = environ.get('HBNB_TYPE_STORAGE', 'file')
if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
