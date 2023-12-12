import os
import json
from pathlib import Path
import shutil
import re


class InMemoryFileSystem:
    def __init__(self):
        self.root = {}
        self.current_dir = os.getcwd()
    
    def mkdir(self, path):
        try:
            os.makedirs(os.path.join(os.getcwd(), path))
        except FileExistsError:
            print(f"Directory already exists: {path}")

    def cd(self, path):
        try:
            if str(path) == "..":
                os.chdir(Path(str(os.getcwd())).parent)
            else:
                os.chdir(os.path.join(os.getcwd(),path))
        except FileNotFoundError:
            print("File not found")
           

    def ls(self, path):
        full_path = Path(path) if path else os.getcwd()
        try:
            if full_path!=None:
                for filename in os.listdir(full_path):
                    print(filename)
            else:
                raise FileNotFoundError
        except Exception as e:
            raise Exception(f"Error listing files in {full_path}: {e}")

    def grep(self, pattern, path):
        try:
            full_path = os.path.join(os.getcwd(),path)

            with open(full_path, 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    if re.search(pattern, line):
                        print(f"{full_path}:{line_number}: {line.strip()}")
        except FileNotFoundError:
            print(f"File not found: {path}")

    def cat(self, path):
        full_path = os.path.join(os.getcwd(),path)
        try:
            with open(full_path, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"File not found: {os.path.join(os.getcwd(),path)}")

    def touch(self, path):
        full_path = os.path.join(os.getcwd(),path)
        with open(full_path, 'w'):
            pass

    def echo(self,path,text):
        full_path = os.path.join(os.getcwd(),path)
        final_str = " ".join(text)
        with open(full_path, 'w') as file:
            file.write(final_str)

    def mv(self, source, destination):
        source_full = os.path.join(os.getcwd(),source)
        dest_full = os.path.join(os.getcwd(),destination)
        try:
            if os.path.isdir(source):
                shutil.move(source_full, dest_full)
            else:
                shutil.move(source_full, dest_full)
        except FileExistsError:
            print("Fild don't exist")

    def cp(self, source, destination):
        full_source_path = os.path.join(os.getcwd(),source)
        full_destination_path = os.path.join(os.getcwd(),destination)
        try:
            if os.path.isfile(full_source_path):
                shutil.copy2(full_source_path, full_destination_path)
            elif os.path.isdir(full_source_path):
                shutil.copytree(full_source_path, full_destination_path)
            else:
                print(f"Source path does not exist: {full_source_path}")
        except FileExistsError:
            print("File not exists")

    def rm(self, path):
        full_path = os.path.join(os.getcwd(),path)
        try:
            if os.path.isfile(full_path):
                os.remove(full_path)
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                print(f"Path does not exist: {full_path}")
        except FileNotFoundError:
            print("File not found")

    def save_state(self, path):
        fullpath = os.path.join(os.getcwd(),path)
        with open(fullpath, 'w') as state_file:
            json.dump({'current_directory': os.getcwd(), 'file_system': os.getcwd()}, state_file)

    def load_state(self, path):
        fullpath = os.path.join(os.getcwd(),path)
        with open(fullpath, 'r') as f:
            state_data = json.load(f)
            print(f"State loaded successfully from {state_data['current_directory']}")
            os.chdir(state_data['current_directory'])

    