import os

from Exceptions.InvalidDateError import InvalidDateError
from Exceptions.InvalidSelectError import InvalidSelectError


class FileHandler:
    def __init__(self, path: str):
        self.file = None
        self.root_path = path

    def GetFilesFromRootDirectory(self) -> list:
        file_paths = []
        for file in os.listdir(self.root_path):
            file_paths.append(self.root_path + "/"+  file)
        return file_paths

    def SelectFile(self):
        print("\n   Please choose The file to work with:")
        files = self.GetFilesFromRootDirectory()
        for i in range(1, len(files) + 1):
            print(f"\t{i}. {files[i - 1]}")
        try:
            try:
                user_input = int(input("   Type number of file: "))
                if user_input < 1 or user_input > len(files):
                    raise InvalidSelectError(f"   Invalid selection: you can chose numbers from 1 to {len(files)}")
                self.file = files[user_input-1]
            except ValueError:
                raise InvalidSelectError(f"   Invalid selection: you can chose numbers from 1 to {len(files)}")
        except InvalidSelectError as e:
            print(e)
            return self.SelectFile()

    def saveFile(self, tasks):
        with open(self.file, 'w') as file:
            for task in tasks:
                file.write(str(task) + '\n')
        pass
