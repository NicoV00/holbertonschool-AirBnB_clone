#!/usr/bin/python3
"""Import the BaseModel class"""


from models.base_model import BaseModel

"""Define the Review class that inherits from BaseModel"""
class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""