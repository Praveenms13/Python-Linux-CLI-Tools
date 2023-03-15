#! /usr/bin/python3

class Arguement:
    def __init__(self, args):
        self.command = []
        self.options = []
        self.optionValues = {} # Dict / Set = Unique No Repeating Values
        self.args = args
        # print("args: ", self.args)

        for arg in self.args:
            if "-" in arg:
               if "=" in arg:
                   pair = arg.split("=")
                   self.options.append(pair[0]) # Appending the Key to the List
                   self.optionValues[pair[0]] = pair[1] # Appending the Key and Value to the Dict
               else:
                   self.options.append(arg)
            else:
                self.command.append(arg)

        # Check if the command and options are correct
        # print(f"command: {self.command}")
        # print(f"options: {self.options}")
        # print(f"optionValues: {self.optionValues}")

    # ------------------------------------------------------------
    # arg.hasOptions(["-l", "-h"])
    def hasOptions(self, options: list):
        userOptions = set(self.options)
        requiredOptions = set(options)
        return list(requiredOptions & userOptions)
    
    def hasOption(self, option, default=False):
        if option in self.hasOptions([option]):
            return True
        return default
    
    def hasOptionValue(self, option):
        if option in self.optionValues:
            return option in self.optionValues
        return False
    # ------------------------------------------------------------
    def hasCommands(self, command):
        # if command in self.command:
        #     return True
        # return default
        userCommand = set(self.command)
        requiredCommand = set([command])
        return list(requiredCommand & userCommand)

    def hasCommand(self, command, default=False):
        if command in self.hasCommands(command):
            return True
        return default
    # ------------------------------------------------------------
    def getOptionValue(self, option, default=None):
        if option in self.optionValues:
            # print("option: ", option)
            # print("optionValues: ", self.optionValues[option])
            return self.optionValues[option]
        return default
    # ------------------------------------------------------------





    