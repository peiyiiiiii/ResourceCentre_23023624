from inventory.item import Item

class Laptop(Item):
# Refactor (E): Extract duplicate attributes and methods.
# There are several common attributes and methods in
# Camera.py and Laptop.py. Extract these common attributes
# and methods into a super class, named item.py
    def __init__(self, assetTag, description, os):
        super().__init__(assetTag, description)
        self._os = os

    def getOS(self):
        return self._os
    
    def __str__(self):
        return super().__str__() +"{:<10}\n".format(self.getOS())
