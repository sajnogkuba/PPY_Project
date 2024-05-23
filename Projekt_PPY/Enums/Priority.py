from enum import Enum


class Priority(Enum):
    HIGH = 1
    NORMAL = 2
    LOW = 3


def getAllPriorities():
    return list(Priority)


def getPriorityByName(name):
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
