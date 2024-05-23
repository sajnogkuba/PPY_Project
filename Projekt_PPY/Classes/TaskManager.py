import os
from datetime import datetime

from Classes.Task import Task
from Enums.Priority import Priority, getAllPriorities
from Exceptions.InvalidDateError import InvalidDateError
from Exceptions.InvalidSelectError import InvalidSelectError


def generateManagersForAllFilesInDir(directory) -> dict:
    managers = dict()
    for file in os.listdir(directory):
        managers[directory + '/' + file] = TaskManager(file)
    return managers


class TaskManager:
    def __init__(self, file):
        self.file = file
        self.tasks = list()

    def addTask(self):
        print("\n ---------------------------------------------------------------------------------------")
        print(f"                            Adding new task to file: {self.file}")
        print(" ---------------------------------------------------------------------------------------")
        name = self.inputNameCreate()
        description = input("   Enter task description for new task: ")
        priority = self.choosePriority()
        deadline = self.inputDeadline()
        completed = False
        task = Task(name, description, priority, deadline, completed)
        self.tasks.append(task)
        pass

    def deleteTask(self):
        print("\n ---------------------------------------------------------------------------------------")
        print(f"                            Deleting task from file: {self.file}")
        print(" ---------------------------------------------------------------------------------------")
        if not self.tasks:
            print("   No tasks yet, first add at least one task")
        else:
            for i in range(1, len(self.tasks) + 1):
                print(f"    {i}. {self.tasks[i - 1]}")
            try:
                try:
                    input_number = int(input(f"   Enter task number 1-{len(self.tasks)}: "))
                    if input_number < 1 or input_number > len(self.tasks):
                        raise InvalidSelectError(
                            f"   Invalid selection: you can chose numbers from 1 to {len(self.tasks)}"
                        )
                    self.tasks.pop(input_number - 1)
                except InvalidSelectError as e:
                    print(f"   {e.message}. Please try again.")
                    return self.deleteTask()
            except InvalidSelectError as e:
                print(e)
                return self.choosePriority()
        pass

    def editTask(self):
        # TODO
        pass

    def filterTasks(self):
        # TODO
        pass

    def viewTasks(self):
        print("\n ---------------------------------------------------------------------------------------")
        print(f"                            Tasks in file: {self.file}")
        print(" ---------------------------------------------------------------------------------------")
        if not self.tasks:
            print("   No tasks yet, first add at least one task")
        else:
            for task in self.tasks:
                print(f"    - {task}")
        pass

    def inputNameCreate(self) -> str:
        name = input("   Enter name for new task: ")
        for task in self.tasks:
            if task.name == name:
                print("  Task already exists, please try another name")
                return self.inputNameCreate()
        return name
        pass

    def choosePriority(self) -> Priority:
        priorities = getAllPriorities()
        for priority in priorities:
            print(f"   {priority.value}. {priority.name}")
        try:
            try:
                input_number = int(input(f"   Enter priority number 1-{len(priorities)}: "))
                return Priority(input_number)
            except ValueError:
                raise InvalidSelectError(f"   Invalid priority number. Please try again")
        except InvalidSelectError as e:
            print(e)
            return self.choosePriority()

    def inputDeadline(self) -> datetime:
        try:
            input_date_str = input("   Enter the start date (DD-MM-YYYY): ")
            date_format = "%m-%d-%Y"
            try:
                date_obj = datetime.strptime(input_date_str, date_format)
            except ValueError:
                raise InvalidDateError("Date format does not match format (DD-MM-YYYY).")
            if date_obj < datetime.now():
                raise InvalidDateError("The date is in the past.")
        except InvalidDateError as e:
            print(f"   {e.message} Please try again")
            return self.inputDeadline()

        return date_obj
        pass
