#!/usr/bin/python3
"""Module FileStorage:
Serializes instances to a JSON file and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    class that serializes instances to a JSON file and
    deserializes JSON file to instances
    Private class attributes:
        __file_path: string, path to the JSON file (ex: file.json)
        __objects: dictionary, empty but will store all objects <class name>.id
    """
    __file_path = "file.json"
    __objects = {}
    dict_class = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """
        Return:
            the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Arg:
            obj: Add a new obj in __objects{}
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects(dictionary{}) to the JSON file
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects({})
        Only if the JSON file (__file_path) exists
        If the file dont exist, no exception should be raised
        """
        try:
            with open(self.__file_path, mode='r', encoding="UTF-8") as file:
                new_obj = json.load(file)
            for key, value in new_obj.items():
                obj = self.dict_class[value["__class__"]](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
        except FileExistsError:
            pass
