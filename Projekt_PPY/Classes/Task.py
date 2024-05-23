import datetime
from Enums.Priority import Priority
from Enums.Status import Status


class Task:
    """
    Represents a task with various attributes.

    Attributes:
        name (str): The name of the task.
        description (str): Description of the task.
        priority (Priority): Priority level of the task (from Enums.Priority).
        category (str): Category of the task.
        deadline (datetime.datetime): Deadline of the task.
        status (Status): Current status of the task (from Enums.Status).
        created_at (datetime.datetime): Timestamp of when the task was created.
        completed_at (datetime.datetime or str): Timestamp of when the task was completed, or '-' if not completed.
    """
    def __init__(self, name: str, description: str, priority: Priority, category: str, deadline: datetime.datetime, status: Status):
        """
        Initializes an instance of Task.

        Args:
            name (str): The name of the task.
            description (str): Description of the task.
            priority (Priority): Priority level of the task (from Enums.Priority).
            category (str): Category of the task.
            deadline (datetime.datetime): Deadline of the task.
            status (Status): Current status of the task (from Enums.Status).
        """
        self.name = name
        self.description = description
        self.priority = priority
        self.category = category
        self.deadline = deadline
        self.status = status
        self.created_at = datetime.datetime.now()
        self.completed_at = '-'
        if status == Status.COMPLETED:
            self.completed_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the task.

        Returns:
            str: String representation of the task.
        """
        return (f'Name: {self.name} '
                f' Description: {self.description} '
                f' Priority: {self.priority.name} '
                f' Category: {self.category} '
                f' Deadline: {self.deadline} ' 
                f' Status: {self.status.name} '
                f' Created_at: {self.created_at} '
                f' Completed_at: {self.completed_at} ')
