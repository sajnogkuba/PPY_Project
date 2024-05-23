from enum import Enum


class Status(Enum):
    TO_DO = 1
    IN_PROGRESS = 2
    TESTING = 3
    COMPLETED = 4


def getAllStatuses():
    return list(Status)


def getStatusByName(name):
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


