#!/usr/bin/python3
"""Base model created"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base Class """

    def __init__(self, *args, **kwargs):
        """Initialize base model """
        from . import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Return a string """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update model """
        from . import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary """
        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
