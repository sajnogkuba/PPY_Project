from Enums.Actions import Actions
from Exceptions.InvalidSelectError import InvalidSelectError


def printWelcomeMessage() -> None:
    """
    Prints a welcome message for the Task Management System.

    Returns:
        None
    """
    print("\n ================================== TASKS MANAGER ==================================")
    print("   Welcome to Task Management System! An application to help you manage your tasks.")
    print(" ===================================================================================")
    pass


class UserInterface:
    """
    UserInterface class for interacting with the Task Management System.

    Attributes:
        ACTIONS (dict): Dictionary mapping action numbers to action descriptions.
        actions_count (int): Total number of available actions.
    """
    ACTIONS = {Actions.ADD_TASK.value: "Add Task",
               Actions.DELETE_TASK.value: "Delete Task",
               Actions.EDIT_TASK.value: "Edit Task",
               Actions.FILTER_TASKS.value: "Filter Tasks",
               Actions.VIEW_TASKS.value: "View all Tasks",
               Actions.CHANGES_TASK_STATUS.value: "Change task status",
               Actions.SHOW_STATISTICS.value: "Show statistics",
               Actions.CHANGE_FILE.value: "Change File",
               Actions.EXIT.value: "Exit"}

    def __init__(self):
        """
        Initializes an instance of UserInterface.
        """
        self.actions_count = len(self.ACTIONS)
        pass

    def isCorrectSelection(self, user_input: int) -> None:
        """
        Checks if the user's selection is correct.

        Args:
            user_input (int): User's selection.

        Raises:
            InvalidSelectError: If the selection is not valid.
        Returns:
            None
        """
        if user_input not in self.ACTIONS:
            raise InvalidSelectError(f"Invalid selection: you can chose from 1 to {self.actions_count}")
        pass

    def selectAction(self, file: str) -> Actions:
        """
        Prompts the user to select an action.

        Args:
            file (str): Name of the file being worked on.

        Returns:
            Actions: The selected action.
        """
        print(f"\n   Working on: {file}\n   What would you like to do?")
        for action_number in range(1, self.actions_count + 1):
            print(f"\t{action_number}. {self.ACTIONS[action_number]}")
        try:
            try:
                user_input = int(input("   Type number of action: "))
                self.isCorrectSelection(user_input)
            except ValueError:
                raise InvalidSelectError(f"Invalid selection: you can chose numbers from 1 to {self.actions_count}")
        except InvalidSelectError as e:
            print(e)
            return self.selectAction(file)
        return Actions(user_input)
