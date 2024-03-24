#!/usr/bin/python3
""" This module store object on Engine"""
import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State

class FileStorage:
    """ FileStorage Engine """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ method that return dictionary objects"""
        return self.__objects
    def new(self, obj):
        """ method sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, 'w') as f:
            dic = FileStorage.__objects
            dict_obj = {}
            for k, v in dic.items():
                dict_obj[k] = v.to_dict()
            json.dump(dict_obj, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r', encoding='utf-8') as f:
                    json_str = json.load(f)
                    dic = {}
                    for k, v in json_str.items():
                        if k.startswith("BaseModel"):
                            obj  = BaseModel(**v)
                        elif k.startswith("User"):
                            obj = User(**v)
                        elif k.startswith("Place"):
                            obj = Place(**v)
                        elif k.startswith("Review"):
                            obj = Review(**v)
                        elif k.startswith("Amenity"):
                            obj = Amenity(**v)
                        elif k.startswith("State"):
                            obj = State(**v)
                        elif k.startswith("City"):
                            obj = City(**v)
                        dic[k] = obj
                    FileStorage.__objects = dic
        except:
            pass