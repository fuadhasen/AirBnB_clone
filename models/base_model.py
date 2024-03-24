#!/usr/bin/python3
""" This module provide basemodel class that define all common attribute for all class"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """ Base class for all classes """
    def __init__(self, *args, **kwargs):
        """ Base class constructor"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        format_str = "%Y-%m-%dT%H:%M:%S.%f"
                        date_obj = datetime.strptime(v, format_str)
                        setattr(self, k, date_obj)
                    else:
                        setattr(self, k, v)  
                 
    def __str__(self):
        """ printable representation of obj"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] =  dic['created_at'].isoformat()
        dic['updated_at'] =  dic['updated_at'].isoformat()
        return dic