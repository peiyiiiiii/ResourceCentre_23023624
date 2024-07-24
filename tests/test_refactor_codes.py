from inventory.inventory import Inventory

class Test_Refactor_Codes:
    #################### Test findAsset(assetTag) ######################
    def test_find_existing_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)

        return_value = test_inventory.findAsset("C001")

        assert return_value.getAssetTag() == "C001"

    def test_find_non_existing_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)

        return_value = test_inventory.findAsset("C004")

        assert return_value == None

    def test_find_existing_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        
        return_value = test_inventory.findAsset("L001")

        assert return_value.getAssetTag() == "L001"

    def test_find_non_existing_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        
        return_value = test_inventory.findAsset("L004")

        assert return_value == None

    ## Test cases for getNotAvailableCamera() and getNotAvailableLaptop() ##
    def test_view_empty_camera_list_for_Not_Available(self):
        test_inventory = Inventory()

        tested_text = test_inventory.getNotAvailableCamera()
        
        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        actual_text += "There is no camera to display."
        assert tested_text == actual_text

    def test_view_camera_all_available_for_Not_available(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)
        
        tested_text = test_inventory.getNotAvailableCamera()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        assert tested_text == actual_text

    def test_view_camera_only_not_available(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)
        test_inventory.loanLaptop("C002", "01-01-2025")
        test_inventory.loanLaptop("C003", "01-01-2025")
        
        tested_text = test_inventory.getNotAvailableCamera()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C002", "Test camera 2", "No", "01-01-2025", 10)
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C003", "Test camera 3", "No", "01-01-2025", 6)
        assert tested_text == actual_text
        
    def test_view_empty_laptop_list_for_Not_Available(self):
        test_inventory = Inventory()

        tested_text = test_inventory.getNotAvailableLaptop()
        
        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "There is no laptop to display."
        assert tested_text == actual_text

    def test_view_laptop_all_available_for_Not_available(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        
        tested_text = test_inventory.getNotAvailableLaptop()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        assert tested_text == actual_text
        
    def test_view_laptop_only_not_available(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        test_inventory.loanLaptop("L002", "01-01-2025")
        test_inventory.loanLaptop("L003", "01-01-2025")
        
        tested_text = test_inventory.getNotAvailableLaptop()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L002", "Test Laptop 2", "No", "01-01-2025", "MACOS")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L003", "Test Laptop 3", "No", "01-01-2025", "WINXP")
        assert tested_text == actual_text