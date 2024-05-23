from Classes.UserInterface import UserInterface, printWelcomeMessage
from Classes.FileHandler import FileHandler
from Enums.Actions import Actions
from Classes.TaskManager import generateManagersForAllFilesInDir

# Directory containing task files
TASK_FILES_DIR = "TaskFiles"

# Generate task managers for all files in the directory
managers = generateManagersForAllFilesInDir(TASK_FILES_DIR)
# Load tasks for each manager
for manager in managers.values():
    manager.loadTasks(TASK_FILES_DIR)

# Initialize FileHandler and UserInterface instances
file_handler = FileHandler(TASK_FILES_DIR)
user_interface = UserInterface()

# Display welcome message
printWelcomeMessage()

# Select a file to work with
file_handler.SelectFile()
current_file = file_handler.file

# Main loop for user interaction
stop = False
while not stop:
    # Prompt user to select an action
    selected_action = user_interface.selectAction(current_file)

    # Perform action based on user's selection
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
            managers[current_file].filterTasks()
            pass
        case Actions.VIEW_TASKS:
            managers[current_file].viewTasks()
            pass
        case Actions.CHANGES_TASK_STATUS:
            managers[current_file].changeTaskStatus()
            pass
        case Actions.SHOW_STATISTICS:
            managers[current_file].showStatistics()
            pass
        case Actions.CHANGE_FILE:
            # Save tasks to the current file
            file_handler.saveFile(managers[current_file].tasks)
            # Select a new file
            file_handler.SelectFile()
            current_file = file_handler.file
        case Actions.EXIT:
            # Save tasks to the current file before exiting
            file_handler.saveFile(managers[current_file].tasks)
            # Set stop flag to exit the loop
            stop = True
