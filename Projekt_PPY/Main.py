from Classes.UserInterface import UserInterface, printWelcomeMessage
from Classes.FileHandler import FileHandler

user_interface = UserInterface(5)
file_handler = FileHandler("TaskFiles/")
printWelcomeMessage()
file_handler.SelectFile()
user_interface.selectAction(file_handler.file)

