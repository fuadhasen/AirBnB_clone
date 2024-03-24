#!/usr/bin/python3
""" This module provide User class"""
from models.base_model import BaseModel

class User(BaseModel):
    """ user class on AirBnb"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""