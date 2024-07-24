class Item():
    def __init__(self, assertTag, description):
        self.__assertTag = assertTag
        self.__description = description
        self._dueDate = ""
        self.__isAvailable = True

    def getAssetTag(self):
        return self.__assertTag
    
    def getDescription(self):
        return self.__description
    
    def getdueDate(self):
        return self._dueDate
    
    def getIsAvailable(self):
        if self.__isAvailable:
            return "Yes"
        else:
            return "No"
        
    def getOpticalZoom(self):
        return self.__opticalZoom
    
    def setDueDate(self, dueDate):
        self._dueDate = dueDate

    def setIsAvailable(self, isAvailable):
        self.__isAvailable = isAvailable

    def __str__(self):
        return "{:<10}{:<30}{:<10}{:<12}".format(
            self.getAssetTag(), self.getDescription(), 
            self.getIsAvailable(), self.getdueDate())
