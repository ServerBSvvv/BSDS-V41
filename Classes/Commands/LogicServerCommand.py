import Configuration
from Classes.Commands.LogicCommand import LogicCommand
from Classes.Utility import Utility


class LogicServerCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def addCommand(self, fields):
        self.writeVint(0)
        LogicCommand.encode(self, fields)

    def decode(calling_instance, fields):
        fields["ID"] = calling_instance.readVint()
        return LogicCommand.decode(calling_instance, fields)
