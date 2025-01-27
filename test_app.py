import unittest
from app import add_numbers, multiply_numbers, write_to_file, read_from_file

class TestAppFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertNotEqual(add_numbers(1, 1), 3)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(4, 5), 20)
        self.assertNotEqual(multiply_numbers(3, 3), 5)

    def test_file_operations(self):
        write_to_file("test.txt", "Hello, World!")
        content = read_from_file("test.txt")
        self.assertEqual(content, "Hello, World!")

        # Reading a non-existent file
        content = read_from_file("non_existent.txt")
        self.assertEqual(content, "File not found.")

if __name__ == "__main__":
    unittest.main()
