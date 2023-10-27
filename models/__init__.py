#!/usr/bin/python3
"""FileStorage instance for your application"""


from models.engine.file_storage import FileStorage

classes = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }
storage = FileStorage()
storage.reload()
