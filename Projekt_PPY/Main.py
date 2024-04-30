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
            # TODO implement methods to add tasks
            pass
        case Actions.DELETE_TASK:
            # TODO implement methods to delete tasks
            pass
        case Actions.EDIT_TASK:
            # TODO implement methods to edit tasks
            pass
        case Actions.FILTER_TASKS:
            # TODO implement methods to filter tasks
            pass
        case Actions.VIEW_TASKS:
            # TODO implement methods to view tasks
            pass
        case Actions.CHANGE_FILE:
            file_handler.SelectFile()
        case Actions.EXIT:
            stop = True

