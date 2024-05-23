import os
from Exceptions.InvalidSelectError import InvalidSelectError


class FileHandler:
    """
    Class for handling files.

    Attributes:
        file (str): Path to the selected file.
        root_path (str): Path to the root directory from which files are fetched.
    """

    def __init__(self, path: str):
        """
        Initializes an instance of FileHandler.

        Args:
            path (str): Path to the root directory from which files are fetched.
        """
        self.file = None
        self.root_path = path

    def GetFilesFromRootDirectory(self) -> list:
        """
        Retrieves a list of paths to all files in the root directory.

        Returns:
            list: List of file paths.
        """
        file_paths = []
        for file in os.listdir(self.root_path):
            file_paths.append(self.root_path + "/" + file)
        return file_paths

    def SelectFile(self):
        """
        Allows the user to select a file to work with.

        Raises:
            InvalidSelectError: When the user provides an invalid file number.

        Returns:
            None
        """
        print("\n   Please choose The file to work with:")
        files = self.GetFilesFromRootDirectory()
        for i in range(1, len(files) + 1):
            print(f"\t{i}. {files[i - 1]}")
        try:
            try:
                user_input = int(input("   Type number of file: "))
                if user_input < 1 or user_input > len(files):
                    raise InvalidSelectError(f"   Invalid selection: you can chose numbers from 1 to {len(files)}")
                self.file = files[user_input - 1]
            except ValueError:
                raise InvalidSelectError(f"   Invalid selection: you can chose numbers from 1 to {len(files)}")
        except InvalidSelectError as e:
            print(e)
            return self.SelectFile()

    def saveFile(self, tasks):
        """
         Saves a list of tasks to a file.

         Args:
             tasks (list): List of tasks to save.

         Returns:
             None
         """
        with open(self.file, 'w') as file:
            for task in tasks:
                file.write(str(task) + '\n')
        pass

    def loadContent(self):
        """
        Loads the content of a file.

        Returns:
            str: Content of the file.
        """
        with open(self.root_path, 'r') as file:
            return file.read()
