#!/usr/bin/python3
"""Base model created"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base Class"""

    def __init__(self, *args, **kwargs):
        """Initialize base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime. strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update model"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary"""
        dict = self.__dict__
        dict["__class__"] = type(self).__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
