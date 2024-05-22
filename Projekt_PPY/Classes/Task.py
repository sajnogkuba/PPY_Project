import datetime

from Enums.Priority import Priority


class Task:
    def __init__(self, name: str, description: str, priority: Priority, deadline: datetime.datetime, completed: bool):
        self.name = name
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = completed

    def __str__(self):
        return (f'Name: {self.name},'
                f' Description: {self.description},'
                f' Priority: {self.priority.name}, '
                f' Deadline: {self.deadline}' 
                f' Completed: {self.completed}')
