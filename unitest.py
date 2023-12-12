import unittest
import os
from filesystem import InMemoryFileSystem

class TestInMemoryFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = InMemoryFileSystem()

    def test_mkdir(self):
        self.file_system.mkdir("test_directory")
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), "test_directory")))
        
    def test_cd(self):
        test_directory_path = os.path.join(os.getcwd(), "test_directory")
        os.makedirs(test_directory_path)  
        self.file_system.cd("test_directory")
        self.assertEqual(os.getcwd(), test_directory_path)
        
    def test_ls(self):
        self.file_system.mkdir("test_directory")
        self.file_system.ls(os.getcwd())  
    
    def test_grep(self):
        file_content = ["This","is","a","test","file","with","some","content","that","we","can","search."]
        final_txt = " ".join(file_content)
        self.file_system.echo("test_file.txt", final_txt)
        self.file_system.grep("test", "test_file.txt")  

    def test_cat(self):
        file_content = ["This","is","the","content","of","the","file."]
        final_txt = " ".join(file_content)
        self.file_system.echo("test_file.txt", final_txt)
        self.file_system.cat("test_file.txt")  

    def test_touch(self):
        self.file_system.touch("new_file.txt")
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), "new_file.txt")))

    def test_echo(self):
        text = ["This","is","a","test."] #We are using list because when we enter input in terminal we get output in list so to convert the list into string we implement join method.
        final_txt = " ".join(text)
        self.file_system.echo("output.txt", text)
        file_path = os.path.join(os.getcwd(), "output.txt")
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, "r") as file:
            content = file.read()
            self.assertEqual(content, final_txt)


    def test_rm(self):
        self.file_system.touch("file_to_remove.txt")
        self.file_system.rm("file_to_remove.txt")
        self.assertFalse(os.path.exists(os.path.join(os.getcwd(), "file_to_remove.txt")))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
