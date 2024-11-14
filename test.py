import unittest
from string_operation import Sring_operations

class TestStringOperations(unittest.TestCase):

    def setUp(self):
        # This method is run before each test; useful for setup code.
        self.str_ops = Sring_operations()

    def test_concatenate(self):
        # Test string concatenation
        result = self.str_ops.concatenate("Hello, ", "world!")
        self.assertEqual(result, "Hello, world!")
        
        result = self.str_ops.concatenate("", "test")
        self.assertEqual(result, "test")
        
        result = self.str_ops.concatenate("123", "456")
        self.assertEqual(result, "123456")

    def test_to_upper(self):
        # Test converting to uppercase
        result = self.str_ops.to_upper("hello")
        self.assertEqual(result, "HELLO")
        
        result = self.str_ops.to_upper("Python")
        self.assertEqual(result, "PYTHON")

    def test_to_lower(self):
        # Test converting to lowercase
        result = self.str_ops.to_lower("HELLO")
        self.assertEqual(result, "hello")
        
        result = self.str_ops.to_lower("Python")
        self.assertEqual(result, "python")

    def test_reverse_string(self):
        # Test reversing a string
        result = self.str_ops.reverse_string("abcd")
        self.assertEqual(result, "dcba")
        
        result = self.str_ops.reverse_string("racecar")
        self.assertEqual(result, "racecar")  # Palindrome test

    def test_get_length(self):
        # Test getting string length
        result = self.str_ops.get_length("Hello")
        self.assertEqual(result, 5)
        
        result = self.str_ops.get_length("")
        self.assertEqual(result, 0)

if _name_ == '_main_':
    unittest.main()