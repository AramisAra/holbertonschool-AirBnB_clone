#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city in the AirBnB clone project."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
