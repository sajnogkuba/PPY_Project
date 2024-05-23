from enum import Enum


class Priority(Enum):
    """
    Enumeration class defining different priority levels for tasks.

    Attributes:
        HIGH (int): High priority level.
        NORMAL (int): Normal priority level.
        LOW (int): Low priority level.
    """
    HIGH = 1
    NORMAL = 2
    LOW = 3


def getAllPriorities():
    """
    Returns a list of all priority levels.

    Returns:
        list: List of all priority levels.
    """
    return list(Priority)


def getPriorityByName(name):
    """
    Returns the priority level corresponding to the given name.

    Args:
        name (str): Name of the priority level.

    Returns:
        Priority: Priority level corresponding to the given name.
    """
    match name:
        case "HIGH":
            return Priority.HIGH
            pass
        case "NORMAL":
            return Priority.NORMAL
            pass
        case "LOW":
            return Priority.LOW
            pass
