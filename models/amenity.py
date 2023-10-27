#!/usr/bin/python3
"""Import the BaseModel class"""


from models.base_model import BaseModel

"""Define the Amenity class that inherits from BaseModel"""
class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)