#!/usr/bin/python3
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

    def do_show(self, args):
        """
             Prints the string representation of an instance
             based on the class name and id.
        """
        if not args or args is None:
            print("** class name missing **")
            return
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
        if not args or args is None:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
