import unittest
import os
import subprocess

# from .base_node_visitor import BaseNodeVisitor


class BaseTest(unittest.TestCase):

    def test_commons(self):
        all_filenames = os.listdir("./models")

        def recursion(all_file):
            exceptions = ['__init__.py', '__pycache__']
            for filename in all_file:
                if exceptions[0] not in filename and exceptions[1] not in filename:
                    print(filename)
                    path = os.path.join("./models", filename)
                    if not self.is_dir(path):
                        self.first_line_shebang_test(path)
                        # self.file_is_executable_test(path)
                        self.pycode_style_test(path)
                        # self.all_doc_test(path)
                    else:
                        all_filenames = os.listdir("./models/" + filename)
                        all_filenames = [filename + '/' +
                                         file for file in all_filenames]
                        recursion(all_filenames)
        recursion(all_filenames)

    def is_dir(self, path):
        """
        Check whether the given path is a file or a directory.

        Args:
            path (str): Path to check.

        Returns:
            str: 'file' if the path is a directory,
            return 1 while 0 if file or doesn't exist
        """
        print("TEST", path, os.path.isdir(path))
        if os.path.isdir(path):
            return 1
        return 0

    def first_line_shebang_test(self, path):
        """ Testing the first line of a specific file is expected. """
        shebang = "#!/usr/bin/python3\n"

        with open(path, 'r') as file:
            lines = file.readlines()
        if len(lines) == 0:
            print(f"Error: Your file {path} has no content.")

        self.assertEqual(lines[0], shebang, f"{path} has no shebang {shebang}")

    def file_is_executable_test(self, path: str):
        """ Testing the target file is executable. """

        is_executable = os.access(path, os.X_OK)
        self.assertTrue(is_executable, f"{path} should be executable")

    def pycode_style_test(self, path: str):
        """ Testing  a specific file meet pep8 requirements """

        command = ["pycodestyle", path]
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if pycodestyle result is successful (exit code 0)
        self.assertEqual(result.returncode, 0,
                         f"pycodestyle check failed:\n{result.stdout}")

    # def all_doc_test(self, path: str) -> None:
    #     """ Testing  module, classes and functions in the module
    #     are all documented.
    #     """
    #     with open(path, 'r') as file:
    #         read_content = file.read()
    #     visitor = BaseNodeVisitor(read_content)
    #     for doc_dict in visitor.doc_list:
    #         self.assertTrue(
    #             doc_dict["doc"], f"Your {doc_dict['name']} has no documentation.")
