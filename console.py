#!/usr/bin/python3
"""This module is Entry point of our command INTERPRETER"""
import cmd
import json
import sys
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ Entry point of our consol.
        Application.
    """
    prompt = '(hbnb) '
    def do_quit(self, line):
        """ quite method """
        return True

    def help_quit(self):
        """ help method """
        print("Quit command to exit the program")
        print()

    def do_EOF(self, line):
        """ EOF method """
        return True

    def do_create(self, line):
        """ create command """
        # print(line)
        if not line:
            print("** class name missing **")
        elif line == "BaseModel":
            model = BaseModel()
            model.save()
            print(model.id)
        elif line  == "User":
            model = User()
            model.save()
            print(model.id)
        elif line  == "Place":
            model = Place()
            model.save()
            print(model.id)
        elif line  == "City":
            model = City()
            model.save()
            print(model.id)
        elif line  == "State":
            model = State()
            model.save()
            print(model.id)
        elif line  == "Amenity":
            model = Amenity()
            model.save()
            print(model.id)
        elif line  == "Review":
            model = Review()
            model.save()
            print(model.id)
        elif line is not BaseModel:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ show command"""
        cls_arr = ["BaseModel", "User", "Place", "Amenity", "City", "State", "Review"]
        if not line:
            print("** class name missing **")
        else:
            arr = []
            for i in line.split(" "):
                arr.append(i)

            if arr[0] not in cls_arr:
                 print("** class doesn't exist **")
            else:
                if len(arr) == 1:
                    print("** instance id missing **")
                else:
                    flag = 0
                    wanted_key = "{}.{}".format(arr[0], arr[1])
                    dic = FileStorage._FileStorage__objects
                    for k, v in dic.items():
                        if wanted_key == k:
                            obj_str = v.__str__()
                            print(obj_str)
                            flag = 1
                            break
                    if flag != 1:
                        print("** no instance found **")

    def do_destroy(self, line):
        """ destroy command"""
        cls_arr = ["BaseModel", "User", "Place", "Amenity", "City", "State", "Review"]
        if not line:
            print("** class name missing **")
        else:
            arr = []
            for i in line.split(" "):
                arr.append(i)

            if arr[0] not in cls_arr:
                 print("** class doesn't exist **")
            else:
                if len(arr) == 1:
                    print("** instance id missing **")
                else:
                    wanted_key = "{}.{}".format(arr[0], arr[1])
                    dic = FileStorage._FileStorage__objects
                    new_dic = {}
                    flag = 0
                    for k, v in dic.items():
                        if wanted_key != k:
                            # how to delete
                            new_dic[k] = v
                        else:
                            flag = 1
                    if flag == 1:
                        FileStorage._FileStorage__objects = new_dic
                        storage.save()
                    if flag == 0:
                        print("** no instance found **")

    def do_all(self, line):
        """ all command"""
        cls_arr = ["BaseModel", "User", "Place", "Amenity", "City", "State", "Review"]
        if not line or line in cls_arr:
            dic = FileStorage._FileStorage__objects
            # print(dic)
            str_arr = []
            for k, v in dic.items():
                obj_str = v.__str__()
                # print(obj_str)
                final_str = "{}".format(obj_str)
                str_arr.append(final_str)
            print(str(str_arr))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ update command"""
        cls_arr = ["BaseModel", "User", "Place", "Amenity", "City", "State", "Review"]
        if not line:
            print("** class name missing **")
        else:
            arr = []
            for i in line.split(" "):
                arr.append(i)

            if arr[0] not in cls_arr:
                 print("** class doesn't exist **")
            else:
                if len(arr) == 1:
                    print("** instance id missing **")
                else:
                    wanted_key = "{}.{}".format(arr[0], arr[1])
                    dic = FileStorage._FileStorage__objects
                    flag = 0
                    for k, v in dic.items():
                        if wanted_key == k:
                            # how to update
                            flag = 1
                            if len(arr) < 3:
                                print("** attribute name missing **")
                                break
                            if len(arr) < 4:
                                print("** value missing **")
                                break
                            attr_name = str(arr[2])
                            attr_value = arr[3].strip('"')
                            setattr(v, attr_name, attr_value)
                            storage.save()

                    if flag == 0:
                        print("** no instance found **")

if __name__ ==  "__main__":
    HBNBCommand().cmdloop()