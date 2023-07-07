#!/usr/bin/python3
""" Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter
    """
    models = ["BaseModel"]
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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it(to the JSON file),
        and prints the id
        Usage: create <model>
        """
        if len(args) == 0:
            print("** class name missing **")
            return

        args = args.split(' ')[0]
        if args not in HBNBCommand.models:
            print("** class doesn't exist **")
            return

        new_instance = eval(args)()
        new_instance.save()
        print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
