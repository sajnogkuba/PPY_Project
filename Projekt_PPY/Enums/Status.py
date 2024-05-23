from enum import Enum


class Status(Enum):
    """
    Enumeration class defining different status options for tasks.

    Attributes:
        TO_DO (int): Task is to be done.
        IN_PROGRESS (int): Task is in progress.
        TESTING (int): Task is being tested.
        COMPLETED (int): Task is completed.
    """

    TO_DO = 1
    IN_PROGRESS = 2
    TESTING = 3
    COMPLETED = 4


def getAllStatuses():
    """
    Returns a list of all status options.

    Returns:
        list: List of all status options.
    """
    return list(Status)


def getStatusByName(name):
    """
    Returns the status corresponding to the given name.

    Args:
        name (str): Name of the status.

    Returns:
        Status: Status corresponding to the given name.
    """
    match name:
        case "TO_DO":
            return Status.TO_DO
            pass
        case "IN_PROGRESS":
            return Status.IN_PROGRESS
            pass
        case "TESTING":
            return Status.TESTING
            pass
        case "COMPLETED":
            return Status.COMPLETED
            pass
