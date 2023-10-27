#!/usr/bin/python3
"""Command interpreter for the AirBnB Clone project"""


import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    models.available_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Amenity": Amenity,
        "Place": Place,
        "City": City,
        "Review": Review
        }

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to JSON file"""
        if not arg:
            print("** class name missing **")
        elif arg not in models.available_classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.available_classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in models.available_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_key = "{}.{}".format(args[0], args[1])
                all_objs = storage.all()
                if obj_key in all_objs:
                    print(all_objs[obj_key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in models.available_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_key = "{}.{}".format(args[0], args[1])
                all_objs = storage.all()
                if obj_key in all_objs:
                    del all_objs[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        all_objs = storage.all()
        if not arg:
            print([str(value) for value in all_objs.values()])
        else:
            args = arg.split()
            if args[0] not in models.available_classes:
                print("** class doesn't exist **")
            else:
                print([str(value) for key,
                value in all_objs.items() if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in models.available_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj_key = "{}.{}".format(args[0], args[1])
                all_objs = storage.all()
                if obj_key in all_objs:
                    setattr(all_objs[obj_key], args[2], args[3])
                    storage.save()
                else:
                    print("** no instance found **")

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_EOF(self, line):
        """Exit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
