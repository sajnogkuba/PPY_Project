from Classes.UserInterface import UserInterface, printWelcomeMessage
from Classes.FileHandler import FileHandler
from Enums.Actions import Actions

user_interface = UserInterface()
file_handler = FileHandler("TaskFiles/")
printWelcomeMessage()
file_handler.SelectFile()
stop = False
while not stop:
    selected_action = user_interface.selectAction(file_handler.file)
    match selected_action:
        case Actions.ADD_TASK:
            pass
        case Actions.DELETE_TASK:
            pass
        case Actions.EDIT_TASK:
            pass
        case Actions.FILTER_TASKS:
            pass
        case Actions.VIEW_TASKS:
            pass
        case Actions.CHANGE_FILE:
            file_handler.SelectFile()
        case Actions.EXIT:
            stop = True

