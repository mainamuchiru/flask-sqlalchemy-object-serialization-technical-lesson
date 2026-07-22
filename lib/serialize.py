# lib/serialize.py

from pprint import pprint
from marshmallow import Schema, fields

# model

class Dog:
    def __init__(self, name, breed, tail_wagging = False):
        self.name = name
        self.breed = breed
        self.tail_wagging = tail_wagging
    
    def give_treat(self):
        self.tail_wagging = True


    def scold(self):
        self.tail_wagging = False
        
        
# schema
class DogSchema(Schema):
    name = fields.String()
    breed = fields.String()
    tail_wagging = fields.Boolean()
    
dogs = [
    Dog(name="Snuggles", breed="Beagle", tail_wagging=True),
    Dog(name="Wags", breed ="Collie", tail_wagging=False )
]

pprint(DogSchema(many=True).dumps(dogs))

# dog = Dog(name="Snuggles", breed="Beagle", tail_wagging=True)
# #dog_schema = DogSchema(exclude=("breed", ))

# dog_dict = DogSchema(exculde=("breed")).dumps(dog)
# print(dog_dict)

# dog_dict = DogSchema(only=("breed", "name")).dumps(dog)
# print(dog_dict)