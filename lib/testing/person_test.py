import unittest
from unittest.mock import patch
import io
from person import Person  # Replace 'your_module' with the actual module name

class TestPerson(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_name(self, mock_stdout):
        with self.assertRaises(ValueError):
            Person("", "ITC")
        self.assertEqual(mock_stdout.getvalue(), "Name must be string between 1 and 25 characters.\n")

    # Define other test methods similarly

if __name__ == '__main__':
    unittest.main()

