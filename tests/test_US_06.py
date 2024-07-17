from inventory.inventory import Inventory
class Test_US_06:
   ############### Test loan camera ######################
    def test_loan_an_available_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)

        tested_camera = test_inventory.cameraList[0]
        result = test_inventory.loanCamera(tested_camera.getAssetTag(), "08-08-2030")
        
        assert result == True
        assert tested_camera.getDueDate() == "08-08-2030"
        assert tested_camera.getIsAvailable() == "No"

    def test_loan_an_unavailable_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        tested_camera = test_inventory.cameraList[0]
        result = test_inventory.loanCamera(tested_camera.getAssetTag(), "08-08-2030")
        original_date = tested_camera.getDueDate()
        assert result == True

        result2 = test_inventory.loanCamera(tested_camera.getAssetTag(), "01-01-2050")

        assert result2 == False
        assert tested_camera.getDueDate() == original_date
        assert tested_camera.getIsAvailable() == "No"

    def test_loan_not_exists_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)

        result = test_inventory.loanCamera("CC0016", "08-08-2030")

        assert result == False

    def test_loan_camera_with_missing_details(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        tested_camera = test_inventory.cameraList[0]

        result = test_inventory.loanCamera(tested_camera.getAssetTag(), "")

        assert result == False
        assert tested_camera.getDueDate() == ""
        assert tested_camera.getIsAvailable() == "Yes"

    ############### Test loan laptop ######################
    def test_loan_an_available_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")

        tested_laptop = test_inventory.laptopList[0]
        result = test_inventory.loanLaptop(tested_laptop.getAssetTag(), "08-08-2030")

        assert result == True
        assert tested_laptop.getDueDate() == "08-08-2030"
        assert tested_laptop.getIsAvailable() == "No"

    def test_loan_an_unavailable_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        tested_laptop = test_inventory.laptopList[0]
        result = test_inventory.loanLaptop(tested_laptop.getAssetTag(), "08-08-2030")
        original_date = tested_laptop.getDueDate()
        assert result == True

        result2 = test_inventory.loanLaptop(tested_laptop.getAssetTag(), "01-01-2050")
        
        assert result2 == False
        assert tested_laptop.getDueDate() == original_date
        assert tested_laptop.getIsAvailable() == "No"

    def test_loan_not_exists_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")

        result = test_inventory.loanLaptop("CB0016", "08-08-2030")

        assert result == False

    def test_loan_laptop_with_missing_details(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        tested_laptop = test_inventory.laptopList[0]

        result = test_inventory.loanLaptop(tested_laptop.getAssetTag(), "")

        assert result == False
        assert tested_laptop.getDueDate() == ""
        assert tested_laptop.getIsAvailable() == "Yes"
