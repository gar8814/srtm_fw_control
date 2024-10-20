class Menu:
    def __init__(self):
        self.currentMenu = "Main Menu"
        self.leafSelection = None
        self.menuTree = {
            "Main Menu": {
                "options": ["Board Info", "Frequency Counter"],
                "prefix": "",
                "parent": None
            },
            "Board Info": {
                "options": ['axi_boardinfo_efuse', 'axi_boardinfo_dna_low', 'axi_boardinfo_dna_middle', 'axi_boardinfo_dna_high', 'axi_boardinfo_user_reg0', 
                            'axi_boardinfo_user_reg1', 'axi_boardinfo_user_reg2', 'axi_boardinfo_user_reg3', 'axi_boardinfo_user_reg4', 
                            'axi_boardinfo_user_reg5', 'axi_boardinfo_user_reg6', 'axi_boardinfo_user_reg7'],
                "prefix": "axi_boardinfo_",
                "parent": "Main Menu"
            },
            "Frequency Counter": {
                "options": ['freq_count_ctrl_reg', 'freq_count_max_cnt', 'freq_count_base', 'freq_count_clk0', 'freq_count_clk1', 'freq_count_clk2', 'freq_count_clk3', 
                            'freq_count_clk4', 'freq_count_clk5', 'freq_count_clk6', 'freq_count_clk7', 'freq_count_clk8', 'freq_count_clk9', 
                            'freq_count_clk10', 'freq_count_clk11', 'freq_count_clk12', 'freq_count_clk13', 'freq_count_clk14', 'freq_count_clk15', 
                            'freq_count_clk16'],
                "prefix": "freq_count_",
                "parent": "Main Menu"
            }
        }

    def run(self):
        while True:
            self._displayCurrentMenu()
            choice = self._getSelection(self.menuTree[self.currentMenu]["options"])
            
            if choice == 0:
                if self.currentMenu == "Main Menu":
                    print("Exiting...")
                    return 0
                else:
                    self.currentMenu = self.menuTree[self.currentMenu]["parent"]
            else:
                selectedOption = self.menuTree[self.currentMenu]["options"][choice - 1]
                if selectedOption in self.menuTree:
                    self.currentMenu = selectedOption
                else:
                    print(f"Selected: {selectedOption}")
                    leafSelection = selectedOption
                    return selectedOption
    
    def _displayCurrentMenu(self):
        returnOption = "Back"
        if self.currentMenu == 'Main Menu':
            returnOption = "Exit"
        print(f"{self.currentMenu}:")
        options = self.menuTree[self.currentMenu]["options"]
        for index, option in enumerate(options, start=1):
            suffix = option[len(self.menuTree[self.currentMenu]["prefix"]):]
            print(f"\t{index}. {suffix}")
        print("\t0. " + returnOption)
    
    def _getSelection(self, options):
        while True:
            try:
                choice = int(input(">").strip())
                if 0 <= choice <= len(options):
                    return choice
                else:
                    print("Invalid selection, please try again.")
            except ValueError:
                print("Invalid input, please enter an integer.")
