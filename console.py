#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
import re
import json
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

    def default(self, arg):
        """Catch commands if nothing matches"""
        self._precmd(arg)

    def _precmd(self, command):
        """Overrides the precmd method"""
        reg_no_args = r"^(\w*)\.(\w+)(?:\(([^)]*)\))$"
        match = re.search(reg_no_args, command)

        if not match:
            return command
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_args:
            uid = match_uid_args.group(1)
            at_dic = match_uid_args.group(2)
        else:
            uid = args
            at_dic = False

        at_and_value = ""
        if method == "update" and at_dic:
            match_dict = re.search('^({.*})$', at_dic)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_atdic = re.search(
                    '^(?:"([^"]*)")?(?:, (.*))?$', at_dic)
            if match_atdic:
                at_and_value = (match_atdic.group(
                            1) or "") + (match_atdic.group(2) or "")
        cm = method + " " + classname + " " + uid + " " + at_and_value
        self.onecmd(cm)
        return cm

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

    def update_dict(self, classname, uid, _dict):
        """Helping method for update() with a dictionary."""
        s = _dict.replace("'", '"')
        d = json.loads(s)

        if not classname:
            print("** class name missing**")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
