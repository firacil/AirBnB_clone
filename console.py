#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
import re
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
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_ins = storage.classes()[arg]()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, args):
        """
             Prints the string representation of an instance
             based on the class name and id.
        """
        if args == "" or args is None:
            print("** class name missing **")
        else:
            words = args.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    instance = storage.all()[key]
                    print(instance)

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and
            id (save the change into the JSON file).
        """
        if args == "" or args is None:
            print("** class name missing **")
        else:
            words = args.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        if arg != "":
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                ins1 = [str(i) for key, i in storage.all().items()
                        if type(i).__name__ == words[0]]
            print(ins1)

        else:
            ins2 = [str(obj) for key, obj in storage.all().items()]
            print(ins2)

    def do_update(self, args):
        """
            Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """

        if args == "" or args is None:
            print("** class name missing **")
            return

        reg = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(reg, args)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                    attributes = storage.attributes()[classname]
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    elif cast:
                        try:
                            value = cast(value)
                        except ValueError:
                            pass
                    setattr(storage.all()[key], attribute, value)
                    storage.all()[key].save()

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

    def precmd(self, command):
        """Overrides the precmd method"""
        if command == "" or command is None:
            return cmd.Cmd.precmd(self, command)
        reg_no_args = r'\b(\w+\.\w+)\(\)'
        match_no_args = re.search(reg_no_args, command)
        reg_args = r'\b(\w+\.\w+)\(\S+\)'
        match_args = re.search(reg_args, command)
        if match_no_args:
            command = command.replace(".", " ")
            command = command.replace("(", "").replace(")", "")
            command = command.split(" ")
            command = "{} {}".format(command[1], command[0])
        elif match_args:
            command = command.replace(".", " ")
            command = command.replace("(", " ").replace(")", " ")
            command = command.split(" ")
            command = "{} {} {}".format(command[1],
                                        command[0], command[2])
        return cmd.Cmd.precmd(self, command)

    def do_count(self, arg):
        """
            retrieve the number of instances of class
            <class name>.count()
        """
        args = arg.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            m = [
                k for k in storage.all() if k.startswith(
                    args[0] + '.')]
            print(len(m))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
