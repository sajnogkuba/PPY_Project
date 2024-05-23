from Classes.UserInterface import UserInterface, printWelcomeMessage
from Classes.FileHandler import FileHandler
from Enums.Actions import Actions
from Classes.TaskManager import TaskManager, generateManagersForAllFilesInDir

TASK_FILES_DIR = "TaskFiles"
managers = generateManagersForAllFilesInDir(TASK_FILES_DIR)
file_handler = FileHandler(TASK_FILES_DIR)
user_interface = UserInterface()

# TODO Add methods to load tasks from files when starting
printWelcomeMessage()
file_handler.SelectFile()
current_file = file_handler.file
stop = False
while not stop:
    selected_action = user_interface.selectAction(current_file)
    match selected_action:
        case Actions.ADD_TASK:
            managers[current_file].addTask()
            pass
        case Actions.DELETE_TASK:
            managers[current_file].deleteTask()
            pass
        case Actions.EDIT_TASK:
            managers[current_file].editTask()
            pass
        case Actions.FILTER_TASKS:
            # TODO implement methods to filter tasks
            pass
        case Actions.VIEW_TASKS:
            managers[current_file].viewTasks()
            pass
        case Actions.CHANGE_FILE:
            file_handler.SelectFile()
            current_file = file_handler.file
        case Actions.EXIT:
            # TODO Add methods to save files when exit
            stop = True

