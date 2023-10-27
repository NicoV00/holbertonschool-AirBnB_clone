#!/usr/bin/python3


class User(BaseModel):
    """
    User class, inherits from BaseModel.
    Public class attributes:
    - email (str): Empty string for user's email.
    - password (str): Empty string for user's password.
    - first_name (str): Empty string for user's first name.
    - last_name (str): Empty string for user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""