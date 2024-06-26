import os
from datetime import datetime, timedelta
from typing import Any

from Classes.FileHandler import FileHandler
from Classes.Task import Task
from Enums.Priority import Priority, getAllPriorities, getPriorityByName
from Enums.Status import getAllStatuses, Status, getStatusByName
from Exceptions.InvalidDateError import InvalidDateError
from Exceptions.InvalidSelectError import InvalidSelectError


def generateManagersForAllFilesInDir(directory) -> dict:
    """
     Generates TaskManager instances for all files in the specified directory.

     Args:
         directory (str): Path to the directory containing files.

     Returns:
         dict: Dictionary mapping file paths to TaskManager instances.
     """
    managers = dict()
    for file in os.listdir(directory):
        managers[directory + '/' + file] = TaskManager(file)
    return managers


class TaskManager:
    """
    Manages tasks within a file.

    Attributes:
        file (str): Path to the file managed by this TaskManager.
        tasks (list): List of tasks managed by this TaskManager.
    """

    def __init__(self, file):
        """
        Initializes an instance of TaskManager.

        Args:
            file (str): Path to the file managed by this TaskManager.
        """
        self.file = file
        self.tasks = list()

    def addTask(self):
        """
        Adds a new task to the TaskManager.

        Returns:
            None
        """
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
        if name == "" or description == "" or priority == "" or category == "" or deadline == "" or status == "":
            print("    Invalid data. Try again")
            return self.addTask()
        self.tasks.append(task)
        pass

    def deleteTask(self):
        """
            Deletes a task from the TaskManager.

            Returns:
                None
            """
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
        """
        Edits a task in the TaskManager.

        Returns:
            None
        """
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
                    if self.tasks[input_number - 1].status == Status.COMPLETED:
                        raise InvalidSelectError("   Invalid selection: you try to edit completed task")
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
                except ValueError:
                    return
            except InvalidSelectError as e:
                print(e)
                print(f"   {e.message}. Please try again.")
                return self.choosePriority()
        pass
        pass

    def filterTasks(self):
        """
        Filters tasks in the TaskManager.

        Returns:
            None
        """
        result = list()
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
        """
        Displays tasks in the TaskManager.

        Returns:
            None
        """
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
        """
        Prompts the user to input a task name.

        Returns:
            str: The name of the task.
        """
        name = input("   Enter name: ")
        for task in self.tasks:
            if task.name == name:
                print("  Task already exists, please try another name")
                return self.inputNameCreate()
        return name
        pass

    def choosePriority(self) -> str | Priority:
        """
        Prompts the user to choose a priority level.

        Returns:
            Priority: The chosen priority level.
        """
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

    def inputDeadline(self) -> str | datetime:
        """
        Prompts the user to input a deadline for a task.

        Returns:
            datetime: The deadline for the task.
        """
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

    def selectStatus(self) -> str | Status:
        """
        Prompts the user to select a status for a task.

        Returns:
            Status: The selected status.
        """
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
        """
        Prompts the user to select a filter option.

        Returns:
            int: The selected filter option.
        """
        print("   1. Priority")
        print("   2. Complete date")
        print("   3. Status")
        try:
            try:
                input_number = int(input("   What do you want to filter by? "))
            except ValueError:
                raise InvalidSelectError(f"You have to choose number from 1 to 3")
            if input_number not in range(1, 4):
                raise InvalidSelectError(f"You have to choose number from 1 to 3")
            return input_number
        except InvalidSelectError as e:
            print(f"   {e.message}. Please try again.")
            return self.selectFiterOption()
        pass

    def filterByPriority(self) -> list:
        """
        Filters tasks by priority.

        Returns:
            list: Filtered list of tasks.
        """
        result = list()
        priority = self.choosePriority()
        for task in self.tasks:
            if task.priority == priority:
                result.append(task)
        return result
        pass

    def filterByCompleteDate(self) -> list:
        """
        Filters tasks by completion date.

        Returns:
            list: Filtered list of tasks.
        """
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
        """
        Filters tasks by status.

        Returns:
            list: Filtered list of tasks.
        """
        result = list()
        status = self.selectStatus()
        for task in self.tasks:
            if task.status == status:
                result.append(task)
        return result
        pass

    def changeTaskStatus(self):
        """
        Changes the status of a task.

        Returns:
            None
        """
        print("\n ---------------------------------------------------------------------------------------")
        print(f"                            Changing task status in file: {self.file}")
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
                    new_status = self.selectStatus()
                    self.tasks[input_number - 1].status = new_status
                    if new_status == Status.COMPLETED:
                        self.tasks[input_number - 1].completed_at = datetime.now()
                except InvalidSelectError as e:
                    print(f"   {e.message}. Please try again.")
                    return self.deleteTask()
            except InvalidSelectError as e:
                print(e)
                return self.choosePriority()

    def showStatistics(self):
        """
        Displays statistics for tasks.

        Returns:
            None
        """
        print("\n ---------------------------------------------------------------------------------------")
        print(f"                            Statistics for file: {self.file}")
        print(" ---------------------------------------------------------------------------------------")
        print(f"   - Average time of task completion: {self.calculateAvgCompletionTime()}")
        print(f"   - Percentage of tasks completed on time: {self.calculatePercentOfTasksCompletedOnTime()}")
        print(f"   - Percentage distribution of priorities: {self.calculatePrioritiesDistribution()}")
        pass

    def calculateAvgCompletionTime(self) -> str | timedelta | float | Any:
        """
        Calculates the average completion time for tasks.

        Returns:
            float: Average completion time.
        """
        time_deltas = list()
        for task in self.tasks:
            if task.status == Status.COMPLETED:
                time_deltas.append(task.completed_at - task.created_at)
        if len(time_deltas) == 0:
            return "No tasks completed"
        return (sum(time_deltas, timedelta())) / len(time_deltas)
        pass

    def calculatePercentOfTasksCompletedOnTime(self):
        """
        Calculates the percentage of tasks completed on time.

        Returns:
            str: Percentage of tasks completed on time.
        """
        count_of_tasks_completed_on_time = 0
        count_of_tasks = 0
        for task in self.tasks:
            if task.status == Status.COMPLETED:
                count_of_tasks += 1
                if task.completed_at < task.deadline:
                    count_of_tasks_completed_on_time += 1
        if count_of_tasks_completed_on_time == 0:
            return "No tasks completed"
        return f"{round((count_of_tasks_completed_on_time / count_of_tasks) * 100, 2)}%"
        pass

    def calculatePrioritiesDistribution(self) -> str:
        """
        Calculates the distribution of priorities for tasks.

        Returns:
            str: Distribution of priorities.
        """
        priorities_count = {Priority.HIGH: 0, Priority.NORMAL: 0, Priority.LOW: 0}
        for task in self.tasks:
            priorities_count[task.priority] += 1
        return (f" High: {round((priorities_count[Priority.HIGH] / len(self.tasks) * 100), 2)}%"
                f" Normal: {round((priorities_count[Priority.NORMAL] / len(self.tasks) * 100), 2)}%"
                f" High: {round((priorities_count[Priority.LOW] / len(self.tasks) * 100), 2)}%")
        pass

    def loadTasks(self, directory):
        """
        Loads tasks from a file.

        Args:
            directory (str): Directory path containing the file.

        Returns:
            None
        """
        file_handler = FileHandler(directory + '/' + self.file)
        file_content = file_handler.loadContent()
        lines = file_content.split('\n')
        lines.remove("")
        if len(lines) == 0:
            self.tasks = list()
        else:
            tasks = list()
            for line in lines:
                words = line.split()
                name = words[1]
                description = words[3]
                priority = getPriorityByName(words[5])
                category = words[7]
                deadline = datetime.strptime(words[9] + " " + words[10], "%Y-%m-%d %H:%M:%S")
                status = getStatusByName(words[12])
                crated_at = datetime.strptime(words[14] + " " + words[15], "%Y-%m-%d %H:%M:%S.%f")
                completed_at = words[17]
                if completed_at != '-':
                    completed_at = datetime.strptime(words[17] + " " + words[18], "%Y-%m-%d %H:%M:%S.%f")
                new_task = Task(name, description, priority, category, deadline, status)
                new_task.created_at = crated_at
                new_task.completed_at = completed_at
                tasks.append(new_task)
            self.tasks = tasks
