#!/usr/bin/python3
# Import the FileStorage class from the models/engine/file_storage module
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()

# Call the reload() method to load previously saved data from the JSON file
storage.reload()