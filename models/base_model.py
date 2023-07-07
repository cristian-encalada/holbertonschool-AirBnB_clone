#!/usr/bin/python3
"""Module Base Model, parent of all class"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    Class that defines all common attributes/methods for other classes
    Method:
        __init__(self): class constructor
        __str__(self)
        save(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """
        Method:
            __init__(self)
        Public instance attributes:
            id: string - assign with an uuid when an instance is created
            created_at: The current datetime when an instance is created
            updated_up: When an instance is created and it will be updated
        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value, format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, format)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        overriding the __str__ method
        Return:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        updates public instance attribute updated_at with current dttime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dict containing all keys/values of __dict__ of the instance
        """
        new_dict = {}
        new_dict["__class"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        return (new_dict)
