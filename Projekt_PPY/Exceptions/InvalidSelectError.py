class InvalidSelectError(Exception):
    """
    Exception raised for invalid selections made by the user.

    Attributes:
        message (str): Explanation of the error.
    """
    def __init__(self, message):
        """
        Initializes an instance of InvalidSelectError.

        Args:
            message (str): Explanation of the error.
        """
        self.message = message
        super().__init__(self.message)
