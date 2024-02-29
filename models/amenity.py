#!/usr/bin/python3
""" """
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that represents a feature or service provided by a property."""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
