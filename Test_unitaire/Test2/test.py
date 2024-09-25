import unittest
import sys
import os
from unittest.mock import patch
from io import StringIO
 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
# Importer la fonction à tester depuis firstName

from firstName import greet_user
class TestGreetUser(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_greetuser(self, mock_stdount,):
        greet_user(name='Diego')
        self.assertEqual(mock_stdount.getvalue().strip(), "Merci Diego !")

    @patch('sys.stdout',new_callable=StringIO)
    @patch('builtins.input', side_effect=['Lily'])
    def test_empty_input(self, mock_input, mock_stdout,):
        with patch('builtins.input', side_effect= ['Lily']):
            greet_user()

    @patch('sys.stdout',new_callable=StringIO)
    @patch('builtins.input', side_effect=[''])
    def test_empty_input(self, mock_input, mock_stdout,):
        with patch('builtins.input', side_effect= ['']):
            greet_user(name='')

        self.assertEqual(mock_stdout.getvalue().strip(), "Vous n'avez pas saisi un prénom valide")
                         
if __name__== '__main__':
    unittest.main()