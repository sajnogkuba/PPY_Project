class InvalidDateError(Exception):
    """
    Exception raised for invalid date formats or dates.

    Attributes:
        message (str): Explanation of the error.
    """
    def __init__(self, message):
        """
        Initializes an instance of InvalidDateError.

        Args:
            message (str): Explanation of the error.
        """
        self.message = message
        super().__init__(self.message)

