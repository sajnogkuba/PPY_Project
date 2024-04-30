from Exceptions.InvalidDateError import InvalidDateError


def printWelcomeMessage() -> None:
    """
    Prints the welcome message for the Task Management System.
    This function displays the name and purpose of the application, formatted with a decorative banner.
    """
    print("\n ================================== TASKS MANAGER ==================================")
    print("   Welcome to Task Management System! An application to help you manage your tasks.")
    print(" ===================================================================================")


class UserInterface:
    """
     A class to manage user interactions within the Task Management System.

     Attributes:
         actions_count (int): The number of available actions to the user.
         ACTIONS (dict): A dictionary mapping action numbers to descriptions.

     Methods:
         __init__(actions_count: int): Initializes a new UserInterface instance.
         isCorrectSelection(user_input: int): Checks if the user's choice is valid.
         selectAction() -> int: Prompts the user to select an action and validates it.
     """
    ACTIONS = {1: "Add Task", 2: "Delete Task", 3: "Edit Task", 4: "Filter Tasks", 5: "View all Tasks"}

    def __init__(self, actions_count: int):
        """
        Initializes a new UserInterface instance with a specified number of actions.

        Parameters:
            actions_count (int): The number of actions that users can choose from.
        """
        self.actions_count = actions_count
        pass

    def isCorrectSelection(self, user_input: int) -> None:
        """
        Checks if the provided user input corresponds to a valid action number
        Parameters:
            user_input (int): The action number entered by the user
        Raises:
            InvalidDateError: If the input is not a valid action number.
        """
        if user_input not in self.ACTIONS:
            raise InvalidDateError(f"Invalid selection: you can chose from 1 to {self.actions_count}")
        pass

    def selectAction(self) -> int:
        """
        Prompts the user to select an action from the available options and validates the selection
        Returns:
            int: The validated action number chosen by the user
        Raises:
            InvalidDateError: If the input is not a valid integer or out of the allowed range.
        """
        print("\n   What would you like to do?")
        for action_number in range(1, self.actions_count + 1):
            print(f"\t{action_number}. {self.ACTIONS[action_number]}")
        try:
            try:
                user_input = int(input("   Type number of action: "))
                self.isCorrectSelection(user_input)
            except ValueError:
                raise InvalidDateError(f"Invalid selection: you can chose numbers from 1 to {self.actions_count}")
        except InvalidDateError as e:
            print(e)
            return self.selectAction()
        return user_input
