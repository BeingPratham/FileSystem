from filesystem import InMemoryFileSystem
from pathlib import Path
import os

fs = InMemoryFileSystem()

while True:
    
    #This will show us current directory and the >> so we know in which directory we are currently in.
    command = input(os.getcwd()+" >> ").split() 

    #This is the function where if we give input as {>> mkdir test} then it will create test directory in specific folder
    if command[0] == "mkdir":
        fs.mkdir(command[1])
    
    #This is cd command here you can give three commands like {/, .., name of directory} eg {>> cd ..}
    elif command[0] == "cd":
        try:
            fs.cd(Path(command[1]))
        except Exception as e:
            print(f"Error changing directory: {e}")
    
    #This is ls command here you can get list of all the files in that directory eg{>> ls}
    elif command[0] == "ls":
        try:
            path = Path(command[1]) if len(command) > 1 else os.getcwd()
            fs.ls(path)
        except Exception as e:
            print(f"Error listing files: {e}")
        
    #By grep you can search the pattern in the file and if there exist any pattern then it will print that eg{>> grep test testing.txt}
    elif command[0] == "grep":
        fs.grep(command[1], command[2])
    elif command[0] == "cat":
        fs.cat(command[1])
    elif command[0] == "touch":
        fs.touch(command[1])
    elif command[0] == "echo":
        fs.echo(command[1], command[2:])
    elif command[0] == "mv":
        fs.mv(command[1], command[2])
    elif command[0] == "cp":
        fs.cp(command[1], command[2])
    elif command[0] == "rm":
        fs.rm(command[1])
    elif command[0] == "save_state":
        fs.save_state(command[1])
    elif command[0] == "load_state":
        fs.load_state(command[1])
    elif command[0] == "exit":
        break
    else:
        print(f"Unknown command: {command[0]}")

print("Exiting...")
