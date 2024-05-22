from enum import Enum


class Priority(Enum):
    HIGH = 1
    NORMAL = 2
    LOW = 3


def getAllPriorities():
    return list(Priority)
