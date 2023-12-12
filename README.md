<h1>🔥 In Memory File System 🔥</h1>

<h3>👉 Introduction:- 😃</h3><h4>The In-Memory File System is a lightweight, command-line-based file system implemented in Python. This project provides a user-friendly interface for users to interact with a file system entirely stored in memory. It supports a range of operations commonly found in traditional file systems, allowing users to navigate directories, create and delete files and directories, and perform various file-related tasks.</h4>

<h3>👉 Modules Used:- </h3>
<h4>📦 OS :- This module provides a way to interact with the operating system. It's used for file and directory operations, changing the current working directory, and handling paths. </h4>
<h4>📦 JSON :- The json module is used for encoding and decoding JSON data. In this project, it's likely used to save and load the state of the file system.</h4>
<h4>📦 PATHLIB :- The Path class from the pathlib module is used for working with file and directory paths in a more object-oriented way. It's used for handling paths in a cross-platform manner.</h4>
<h4>📦 Re :- The re module provides regular expression matching operations. It's used for pattern matching in files, probably in the grep operation.</h4>
<h4>📦 SHUTIL :- The shutil module provides a higher-level interface for file operations. It's used for functions such as moving and copying files and directories. </h4>
<h4>📦 UNITTEST :- The unittest module is part of the Python Standard Library and provides a testing framework. It's used for writing and executing unit tests for the code.</h4>

<h3>👉 Features:- </h3>
<h4>💎 Mkdir:- Creates a new directory. </h4>
Eg:- (>> mkdir foldername)
<h4>💎 Cd:- Changes the current directory. It can also support ".." and also "/" we can change path by defining path also. </h4>
Eg:- (>> cd ..) <br>
     (>> cd /)<br>
     (>> cd foldername1/foldername2)
<h4>💎 ls:- List the contents of the current directory.</h4>
Eg:- (>> ls)
<h4>💎 touch:- Creates a new empty file.</h4>
Eg:- (>> touch filename.txt)
<h4>💎 echo:- Writes a text to the file.</h4>
Eg:- (>> echo filename.txt Hello world, this is test file)
<h4>💎 cat:- Display the contents of the file. </h4>
Eg:- (>> cat filename.txt)
<h4>💎 grep🔥:- Search for a specified pattern in file.</h4>
Eg:- (>> grep test filename.txt)
<h4>💎 mv:- Move a file or directory to another location. </h4>
Eg:- (>> mv filename.txt foldername1)
<h4>💎 cp:- Copy a file or directory to another location</h4>
Eg:- (>> cp foldername1/filename.txt folername1/foldername2)
<h4>💎 rm:- Remove a file or directory.</h4>
Eg:- (>> rm foldername1/foldername2/filename.txt)
<h4>💎 save_state🔥:- Here you can save the current state of the path by providing the path to it in some file in json.</h4>
Eg:- (>> save_state saved_state)
<h4>💎 load_state🔥:- Here you can load the state of the previously saved path and it will automatically change the directory of saved state.</h4>
Eg:- (>> load_state saved_state)


<h3>👉 How to setup :- </h3>
<h4>1) We need Python. If you don't have python in your system then download python using this link:- https://www.python.org/downloads/</h4>
<h4>2) Clone the repository to a new folder.</h4>
<h4>3. Run the script in the folder where you have cloned this repo using this:- [python main.py] in terminal.</h4>
<h4>4. If you want to run unit tests, than you can write this command in terminal:- [python -m unittest unitest.py] . It will run all the pre-defined test cases created for the features.</h4>
