#!/usr/bin/python3
"""Import the BaseModel class"""


from models.base_model import BaseModel
"""Define the City class that inherits from BaseModel"""


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
