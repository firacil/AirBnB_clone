#!/usr/bin/python3
import cmd
import os
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ class HBNBCommand implementing cmd"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id.

            Args:
                arg
        """
        if not arg or arg is None:
            print("** class name missing **")
            return

        if arg not in storage.classes():
            print("** class doesn't exist **")
            return
        else:
            new_ins = storage.classes()[arg]()
            new_ins.save()
            print(new_ins.id)

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Doesn't do anything on Enter
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
