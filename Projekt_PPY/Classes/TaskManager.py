import os
from datetime import datetime

from Classes.Task import Task
from Enums.Priority import Priority, getAllPriorities
from Enums.Status import getAllStatuses, Status
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
        # TODO if something == "" try again.
        print("\n ---------------------------------------------------------------------------------------")
        print(f"                            Adding new task to file: {self.file}")
        print(" ---------------------------------------------------------------------------------------")
        name = self.inputNameCreate()
        description = input("   Enter task description: ")
        priority = self.choosePriority()
        category = input("   Enter task category: ")
        deadline = self.inputDeadline()
        status = self.selectStatus()
        task = Task(name, description, priority, category, deadline, status)
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
                    new_category = input("   Enter task category: ")
                    new_deadline = self.inputDeadline()
                    new_status = self.selectStatus()
                    if new_name == "":
                        new_name = self.tasks[input_number - 1].name
                    if new_category == "":
                        new_category = self.tasks[input_number - 1].category
                    if new_description == "":
                        new_description = self.tasks[input_number - 1].description
                    if new_priority == "":
                        new_priority = self.tasks[input_number - 1].priority
                    if new_deadline == "":
                        new_deadline = self.tasks[input_number - 1].deadline
                    if new_status == "":
                        new_status = self.tasks[input_number - 1].status
                    created_at = self.tasks[input_number - 1].created_at
                    self.tasks[input_number - 1] = Task(
                        new_name, new_description, new_priority, new_category, new_deadline, new_status
                    )
                    self.tasks[input_number - 1].created_at = created_at
                except InvalidSelectError as e:
                    print(f"   {e.message}. Please try again.")
                    return self.editTask()
            except InvalidSelectError as e:
                print(e)
                return self.choosePriority()
        pass
        pass

    def filterTasks(self):
        print("\n ---------------------------------------------------------------------------------------")
        print(f"                            Filtering tasks in file: {self.file}")
        print(" ---------------------------------------------------------------------------------------")
        if not self.tasks:
            print("   No tasks yet, first add at least one task")
        else:
            selected_filtering_option = self.selectFiterOption()
            match selected_filtering_option:
                case 1:
                    result = self.filterByPriority()
                    pass
                case 2:
                    result = self.filterByCompleteDate()
                    pass
                case 3:
                    result = self.filterByStatus()
                    pass
            if not result:
                print("   No tasks to print.")
            else:
                for task in result:
                    print(f"   - {task}")
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

    def selectStatus(self):
        statuses = getAllStatuses()
        for status in statuses:
            print(f"   {status.value}. {status.name}")
        try:
            try:
                input_text = input(f"   Enter status number 1-{len(statuses)}: ")
                if input_text == "":
                    return input_text
                input_number = int(input_text)
                return Status(input_number)
            except ValueError:
                raise InvalidSelectError(f"   Invalid status number. Please try again")
        except InvalidSelectError as e:
            print(e)
            return self.selectStatus()
        pass

    def selectFiterOption(self) -> int:
        print("   1. Priority")
        print("   2. Complete date")
        print("   3. Status")
        try:
            try:
                input_number = int(input("   What do you want to filter by? "))
            except ValueError:
                raise InvalidSelectError(f"You have to choose number from 1 to 3")
            if input_number not in range(1,4):
                raise InvalidSelectError(f"You have to choose number from 1 to 3")
            return input_number
        except InvalidSelectError as e:
            print(f"   {e.message}. Please try again.")
            return self.selectFiterOption()
        pass

    def filterByPriority(self) -> list:
        result = list()
        priority = self.choosePriority()
        for task in self.tasks:
            if task.priority == priority:
                result.append(task)
        return result
        pass

    def filterByCompleteDate(self) -> list:
        result = list()
        date_format = "%d-%m-%Y"
        input_date_str = input("   Enter the date (DD-MM-YYYY): ")
        try:
            try:
                date_obj = datetime.strptime(input_date_str, date_format)
            except ValueError:
                raise InvalidDateError("Date format does not match format (DD-MM-YYYY).")
        except InvalidDateError as e:
            print(f"   {e.message}. Please try again.")
            return self.filterByCompleteDate()
        for task in self.tasks:
            if task.created_at.date() == date_obj.date():
                result.append(task)
        return result
        pass

    def filterByStatus(self) -> list:
        result = list()
        status = self.selectStatus()
        for task in self.tasks:
            if task.status == status:
                result.append(task)
        return result
        pass
