import datetime

from Enums.Priority import Priority
from Enums.Status import Status


class Task:
    def __init__(self, name: str, description: str, priority: Priority, deadline: datetime.datetime, status: Status):
        self.name = name
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.status = status

    def __str__(self):
        return (f'Name: {self.name},'
                f' Description: {self.description},'
                f' Priority: {self.priority.name}, '
                f' Deadline: {self.deadline}' 
                f' Status: {self.status.name}')
