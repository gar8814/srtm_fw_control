class Menu:
    def __init__(self):
        self.currentMenu = "Main Menu"
        
        # "Menu Name": {
        #   "options": ["option num1", "option num2"], # ** REQUIRED **
        #   "parent" : "Name of Parent Menu", # ** REQUIRED **
        #   "extra options" : ["Read"],
        #   "prefix" : "option ", # removed from beginning of each "option" when displayed
        #   "operation" : "Write " # added to beginning of each "option" when displayed.
        #}
        
        # Output: 
        # Menu Name:
        #   1. Write num1
        #   2. Write num2
        #   3. Read
        #   0. Back
        
        self.menuTree = {
            "Main Menu": {
                "options": ["Board Info", "Frequency Counter", "LTI", "SPI"],
                "parent": None
            },
            "Board Info": {
                "options": ['axi_boardinfo_user_reg5', 'axi_boardinfo_user_reg6', 'axi_boardinfo_user_reg7'],
                "parent": "Main Menu",
                "extra options": ['Read'],
                "prefix": "axi_boardinfo_",
                "operation": "Write "
            },
            "Frequency Counter": {
                "options": ['freq_count_max_cnt'],
                "parent": "Main Menu",
                "extra options": ['Read'],
                "prefix": "freq_count_",
                "operation": "Write "
            },
            "LTI": {
                "options" : ['Send Data Test'],
                "parent": "Main Menu"
            },
            "SPI": {
                "options" : ['Send Master Data', 'Read Sanity', 'Read Status', 'Send Reset'],
                "parent" : 'Main Menu'
            }
        }

 

    def run(self):
        print("INFO: In menu.run()")
        while True:

            self.displayCurrentMenu()
            print("INFO: After menu.DisplayCurrentMenu() call")
            currentSelections = len(self.menuTree[self.currentMenu].get("options", []) + self.menuTree[self.currentMenu].get("extra options", []))
            choice = self._getSelection(currentSelections)
            print(f'choice = {choice}')
            if choice == 0:
                if self.currentMenu == "Main Menu":
                    print("Exiting...")
                    return 0
                else:
                    self.currentMenu = self.menuTree[self.currentMenu]["parent"]
            else:
                if choice > len(self.menuTree[self.currentMenu]["options"]):
                    selectedOption = self.menuTree[self.currentMenu]["extra options"][choice - len(self.menuTree[self.currentMenu]["options"]) - 1]
                    selectedOption = selectedOption + " " + self.currentMenu
                else:
                    selectedOption = self.menuTree[self.currentMenu]["options"][choice - 1]
                if selectedOption in self.menuTree:
                    self.currentMenu = selectedOption
                else:
                    print(f"Selected: {selectedOption}")
                    return selectedOption

    
    def displayCurrentMenu(self):
        print("INFO: in menu.displayCurrentMenu()")
        returnOption = "Back"
        operation = self.menuTree[self.currentMenu].get("operation", "")
        if self.currentMenu == 'Main Menu':
            returnOption = "Exit"
            operation = ""
        
        options = self.menuTree[self.currentMenu].get("options", [])
        prefix = self.menuTree[self.currentMenu].get("prefix", [])
        extraOptions = self.menuTree[self.currentMenu].get("extra options", [])
        
        print(f"{self.currentMenu}:")
        
        optionNumbering = 1
        for option in options:
            suffix = option[len(prefix):]
            print(f"\t{optionNumbering}. {operation}{suffix}")
            optionNumbering += 1
        
        for extraOption in extraOptions:
            print(f"\t{optionNumbering}. {extraOption}")
            
        
        print("\t0. " + returnOption)
    
    def _getSelection(self, options):
        while True:
            try:
                choice = int(input(">").strip())
                if 0 <= choice <= options:
                    return choice
                print("Invalid selection, please try again.")
            except ValueError:
                print("Invalid input, please enter an integer.")
