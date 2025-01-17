import unittest
from hello import say_hello

class Tests_say_hello(unittest.TestCase):
    def test_say_hello(self): 
        self.assertEqual(say_hello("Julia"), "Hello, Julia!")
        self.assertEqual(say_hello("Anastasia"), "Hello, Anastasia!")
        self.assertEqual(say_hello(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()
