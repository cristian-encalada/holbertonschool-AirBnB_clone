#!/usr/bin/python3
"""Module that contains class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
