from inventory.camera import Camera
from inventory.laptop import Laptop
class Inventory():
    pass
    def __init__(self):
        self.cameraList = []
        self.laptopList = []

    def addCamera(self, assetTag, description, opticalzoom):
        # Check for correct values
        correct = True
        if len(assetTag)==0 or len(description)==0 or opticalzoom<0:
            correct = False
            error_message = "Incorrect values."
        # Refactor (C): Extract long methods to findCamera(assetTag),
        # return the found camera, return None if not found.
        # **Don't forget to create test cases for this new method.
        # Check for existing camera
        notExist = True
        for c in self.cameraList:
            currentTag = c.getAssetTag()
            if currentTag == assetTag:
                notExist = False
                error_message = "Asset already exists."
        if correct and notExist:
            new_camera = Camera(assetTag, description, opticalzoom)
            self.cameraList.append(new_camera)
            return True

        else:
            print(error_message)
            return False
    
    def addLaptop(self, assetTag, description, os):
        # Check for correct values
        correct = True
        if len(assetTag)==0 or len(description)==0 or len(os)==0:
            correct = False
            error_message = "Incorrect values."
            
        # Refactor (C): Extract long methods to findLaptop(assetTag),
        # return the found laptop, return None if not found.
        # **Don't forget to create test cases for this new method.
        # Check for existing laptop
        notExist = True
        for l in self.laptopList:
            currentTag = l.getAssetTag()
            if currentTag == assetTag:
                notExist = False
                error_message = "Asset already exists."
            
        if correct and notExist:
            new_laptop = Laptop(assetTag, description, os)
            self.laptopList.append(new_laptop)
            return True
        else:
            print(error_message)
            return False
    
    def getAvailableCamera(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        if len(self.cameraList) == 0:
            output += "There is no camera to display."
        else:
            for i in self.cameraList:
                if i.getIsAvailable() == "Yes":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format( 
                        i.getAssetTag(), i.getDescription(),  
                        i.getIsAvailable(), i.getDueDate(), 
                        i.getOpticalZoom() )
            
        return output
    
    def getAvailableLaptop(self):
        output = ""
        output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        if len(self.laptopList) == 0:
            output += "There is no laptop to display."
        else:
            for i in self.laptopList:
                if i.getIsAvailable() == "Yes":
                    # Refactor (D): Extract duplicate code as __str__()
                    # If __str__() already created, use it.
                    output += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
                        i.getAssetTag(), i.getDescription() , 
                        i.getIsAvailable(), i.getDueDate(), 
                        i.getOS() )
        return output
    
    def loanCamera(self, assetTag, dueDate):
        success = False
        if len(assetTag) > 0 and len(dueDate) > 0:
            # Refactor (C): use findCamera()
            for i in self.cameraList:
                if i.getAssetTag() == assetTag:
                    if i.getIsAvailable() == "Yes":
                        i.setIsAvailable(False)
                        i.setDueDate(dueDate)
                        success = True
        
        return success
    
    def loanLaptop(self, assetTag, dueDate):
        success = False
        if len(assetTag) > 0 and len(dueDate) > 0:
            # Refactor (C): use findcamera()
            for i in self.laptopList:
                if i.getAssetTag() == assetTag:
                    if i.getIsAvailable() == "Yes":
                        i.setIsAvailable(False)
                        i.setDueDate(dueDate)
                        success = True
        
        return success
    
    def returnCamera(self, assetTag):
        success = False
        if len(assetTag) > 0:
            # Refactor (C): use findcamera()
            for i in self.cameraList:
                if i.getAssetTag() == assetTag:
                    if i.getIsAvailable() == "No":
                        i.setIsAvailable(True)
                        i.setDueDate("")
                        success = True
        
        return success
    
    def returnLaptop(self, assetTag):
        success = False
        if len(assetTag) > 0:
            # Refactor (C): use findcamera()
            for i in self.laptopList:
                if i.getAssetTag() == assetTag:
                    if i.getIsAvailable() == "No":
                        i.setIsAvailable(True)
                        i.setDueDate("")
                        success = True
        
        return success
