#!/usr/bin/python3
""" Contains the entry point of the command interpreter
"""
import cmd
from shlex import split
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter
    """
    list_models = ["BaseModel"]
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered
        """
        pass

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        exit()

    def do_quit(self, line):
        """Quit command to exit the program
        """
        quit()

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it(to the JSON file),
        and prints the id
        Usage: create <class_name>
        Example: create BaseModel
        """
        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.list_models:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        Usage: show <class_name> <instance_id>
        Example: show BaseModel 1234-1234-1234
        """
        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.list_models:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instance = models.storage.all().get(key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
