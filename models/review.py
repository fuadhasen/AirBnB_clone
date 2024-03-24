#!/usr/bin/python3
""" This module provide Review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """ Review class on AirBnb"""
    place_id = ""
    user_id = ""
    text = ""