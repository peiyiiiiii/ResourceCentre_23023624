from inventory.item import Item

class Camera(Item):
    # Refactor (E): Extract duplicate attributes and methods.
    # There are several common attributes and methods in
    # Camera.py and Laptop.py. Extract these common attributes
    # and methods into a super class, named item.py
    def __init__(self, assetTag, description, opticalZoom):
        super().__init__(assetTag, description)
    
    def getOpticalZoom(self):
        return self._opticalZoom
    
    def __str__(self):
        return super().__str__() + "{:<10}\n".format(self.getOpticalZoom())