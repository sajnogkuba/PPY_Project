import datetime

from Enums.Priority import Priority
from Enums.Status import Status


class Task:
    def __init__(self, name: str, description: str, priority: Priority, category: str, deadline: datetime.datetime, status: Status):
        self.name = name
        self.description = description
        self.priority = priority
        self.category = category
        self.deadline = deadline
        self.status = status
        self.created_at = datetime.datetime.now()
        self.completed_at = '-'

    def __str__(self):
        return (f'Name: {self.name},'
                f' Description: {self.description},'
                f' Priority: {self.priority.name}, '
                f' Deadline: {self.deadline}' 
                f' Status: {self.status.name}'
                f' Created at: {self.created_at}'
                f' completed at: {self.completed_at}')
