#!/usr/bin/python3
""" Contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter
    """
    prompt = "(hbnb)"

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
