from enum import Enum


class Actions(Enum):
    """
    Enumeration class defining different actions for the Task Management System.

    Attributes:
        ADD_TASK (int): Action to add a new task.
        DELETE_TASK (int): Action to delete a task.
        EDIT_TASK (int): Action to edit a task.
        FILTER_TASKS (int): Action to filter tasks.
        VIEW_TASKS (int): Action to view all tasks.
        CHANGES_TASK_STATUS (int): Action to change the status of a task.
        SHOW_STATISTICS (int): Action to show statistics.
        CHANGE_FILE (int): Action to change the file being worked on.
        EXIT (int): Action to exit the Task Management System.
    """

    ADD_TASK = 1
    DELETE_TASK = 2
    EDIT_TASK = 3
    FILTER_TASKS = 4
    VIEW_TASKS = 5
    CHANGES_TASK_STATUS = 6
    SHOW_STATISTICS = 7
    CHANGE_FILE = 8
    EXIT = 9
