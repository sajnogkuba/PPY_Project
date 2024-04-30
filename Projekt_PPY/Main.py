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
    if selected_action == Actions.EXIT.value:
        stop = True

