#!/usr/bin/python3
"""Base model created"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """Initialize base model"""
        from . import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime. strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
