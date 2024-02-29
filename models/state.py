#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """Represents a state in the AirBnB clone project."""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
