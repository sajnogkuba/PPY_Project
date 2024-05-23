from enum import Enum


class Status(Enum):
    TO_DO = 1
    IN_PROGRESS = 2
    TESTING = 3
    COMPLETED = 4


def getAllStatuses():
    return list(Status)
