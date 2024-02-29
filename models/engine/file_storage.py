#!/usr/bin/python3
""" File Storage Class"""
import json
from models.base_model import BaseModel

class FileStorage():
    """ This class controls file storage """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = type(obj).__name__ + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = {k: BaseModel(**v)
                                  for k, v in json.load(file).items() + ""}
        except Exception:
            pass
