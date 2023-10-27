#!/usr/bin/python3
"""Command interpreter for the AirBnB Clone project"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

classes = {
    'BaseModel': BaseModel, 'User' : User
}

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to JSON file"""
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_objs = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_objs = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        all_objs = storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        print([str(obj) for key, obj in all_objs.items() if key.split('.')[0] == class_name])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_objs = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass
        setattr(all_objs[key], attribute_name, attribute_value)
        all_objs[key].save()

    def emptyline(self):
        """Override emptyline to do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()