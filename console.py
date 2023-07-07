#!/usr/bin/python3
""" Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter
    """
    list_models = ["BaseModel", "User"]
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
        args = line.split()
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
        args = line.split()
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

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Usage: destroy <class_name> <instance_id>
        Example: destroy BaseModel 1234-1234-1234
        """
        args = line.split()
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
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        Example: all BaseModel or all.
        """
        list_string = []
        args = line.split()
        if len(args) == 0:
            obj = models.storage.all()
            for key, value in obj.items():
                obj_str = str(obj[key])
                list_string.append(obj_str)
            print(list_string)
        elif args[0] in HBNBCommand.list_models:
            obj = models.storage.all()
            for key, value in obj.items():
                if args[0] in key:
                    obj_str = str(obj[key])
                    list_string.append(obj_str)
            print(list_string)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Example: update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.list_models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            if key in models.storage.all():
                setattr(models.storage.all()[key], args[2], cast(args[3]))
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
