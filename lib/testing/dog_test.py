import unittest
from unittest.mock import patch
import io
from dog import Dog # Replace 'your_module' with the actual module name

class TestDog(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_name(self, mock_stdout):
        with self.assertRaises(ValueError):
            Dog("", "Labrador")
        self.assertEqual(mock_stdout.getvalue(), "Name must be string between 1 and 25 characters.\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_breed(self, mock_stdout):
        with self.assertRaises(ValueError):
            Dog("Rex", "Not a valid breed")
        self.assertEqual(mock_stdout.getvalue(), "Breed must be in list of approved breeds.\n")

    # Add other tests for name length and type here

if __name__ == '__main__':
    unittest.main()
