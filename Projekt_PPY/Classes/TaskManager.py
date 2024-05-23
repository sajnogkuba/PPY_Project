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
        description = input("   Enter task description: ")
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
        print("\n ---------------------------------------------------------------------------------------")
        print(f"                            Editing task from file: {self.file}")
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
                    print(f"   Please type in new data for task: {self.tasks[input_number - 1]}"
                          f". If you don't want to change something don't type anything and pres enter")
                    new_name = self.inputNameCreate()
                    new_description = input("   Enter task description: ")
                    new_priority = self.choosePriority()
                    new_deadline = self.inputDeadline()
                    if new_name == "":
                        new_name = self.tasks[input_number - 1].name
                    if new_description == "":
                        new_description = self.tasks[input_number - 1].description
                    if new_priority == "":
                        new_priority = self.tasks[input_number - 1].priority
                    if new_deadline == "":
                        new_deadline = self.tasks[input_number - 1].deadline
                    new_status = self.tasks[input_number - 1].completed
                    self.tasks[input_number - 1] = Task(new_name, new_description, new_priority, new_deadline, new_status)
                except InvalidSelectError as e:
                    print(f"   {e.message}. Please try again.")
                    return self.editTask()
            except InvalidSelectError as e:
                print(e)
                return self.choosePriority()
        pass
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
        name = input("   Enter name: ")
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
                input_text = input(f"   Enter priority number 1-{len(priorities)}: ")
                if input_text == "":
                    return input_text
                input_number = int(input_text)
                return Priority(input_number)
            except ValueError:
                raise InvalidSelectError(f"   Invalid priority number. Please try again")
        except InvalidSelectError as e:
            print(e)
            return self.choosePriority()

    def inputDeadline(self) -> datetime:
        try:
            input_date_str = input("   Enter the deadline (DD-MM-YYYY): ")
            if input_date_str == "":
                return input_date_str
            date_format = "%d-%m-%Y"
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
