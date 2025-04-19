# prototype.py
import copy

class ReviewTemplate:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

    def clone(self):
        return copy.deepcopy(self)

 

