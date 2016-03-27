import sys
import unittest

from functions_review import *

class TestFunctionsReview(unittest.TestCase):

    def test_division(self):
        num1 = 42
        num2 = 7
        self.assertEqual(division(42,7), 6)

    def test_greeting(self):
        self.assertEqual(greeting("Hi There","Susan"), "Hi There Susan!")
        self.assertEqual(greeting("Greetings","Earthling"), "Greetings Earthling!")

    def test_return_a_value(self):
        self.assertEqual(return_a_value(), "Have a nice day!")
    
    def test_pizza_party(self):
        self.assertEqual(pizza_party(), "Cheese")
        self.assertEqual(pizza_party("Pepperoni"), "Pepperoni")


if __name__ == '__main__':
    unittest.main()
