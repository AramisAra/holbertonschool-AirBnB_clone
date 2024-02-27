#!/usr/bin/python3
""" Class Base_model """
import uuid
import datetime


class BaseModel():
    """
    Class representing the base model for all other models in the project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Unu.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): The unique identifier of the instance.
            created_at (datetime): The date and time when the instance was created.
            updated_at (datetime): The date and time when the instance was last updated.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            if 'created_at' not in kwargs:
                self.created_at = datetime.datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object.
        The string includes the attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object.
        """
        n_dict = dict(self.__dict__)
        n_dict['__class__'] = self.__class__.__name__
        n_dict['created_at'] = self.created_at.isoformat()
        n_dict['updated_at'] = self.updated_at.isoformat()
        return n_dict
