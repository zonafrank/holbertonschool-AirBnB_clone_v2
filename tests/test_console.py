#!/usr/bin/python3
""" """
from unittest.mock import patch
from io import StringIO

from tests.test_models.test_base_model import test_basemodel
from console import HBNBCommand


class test_console(test_basemodel):
    """ """

    def test_class_doc(self):
        """ """
        doc = HBNBCommand.__doc__
        self.assertTrue(doc)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_no_name(self, mock_stdout):
        command = ''
        HBNBCommand().do_show(command)
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_no_class(self, mock_stdout):
        command = 'Fake'
        HBNBCommand().do_show(command)
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_no_id(self, mock_stdout):
        command = 'City'
        HBNBCommand().do_show(command)
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_wrong_id(self, mock_stdout):
        command = 'City 123123'
        HBNBCommand().do_show(command)
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")
