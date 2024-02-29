#!/usr/bin/python3
"""Defines the HNnB console."""
import cmd
import shlex
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""
    prompt = "(hbnb)"
    valid_classes = {
        "BaseModel": BaseModel,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "User": User,
        "Review": Review,
        "State": State
    }


    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_help(self, arg):
        """Provide help for the quit command. """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """
        Create a new instance of BaeModel and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing**")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ 
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance is missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class
        Usage: all [class_name]
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                     print(str(value))
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (value should be without double quotes).
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[key]
        value = args[3].strip("\"")
        setattr(obj, args[2], value)
        obj.save()
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
