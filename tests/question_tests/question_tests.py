#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions

#Part 1.2
from src.question_a.question_a import use_local_variable

class Test_Config(unittest.TestCase):

    def test_use_local_variable(self):
        num = 100
        return num
        self.assertEqual(100, use_local_variable(100))
        

#Part 2.2
from src.question_b.question_b import get_miles_per_hour

class Test_Config(unittest.TestCase):

    def test_get_miles_per_hour(self):
        self.assertEqual(19.883872, get_miles_per_hour(32,60))
        
#Part 3.2
from src.question_c.question_c import get_bonus_pay

class Test_Config(unittest.TestCase):

    def test_get_bonus_pay(self):
        self.assertEqual("Invalid Argument", get_bonus_pay(-1))
        self.assertEqual(10, get_bonus_pay(200))
        self.assertEqual(36, get_bonus_pay(600))
        self.assertEqual(70, get_bonus_pay(1000))
        self.assertEqual(120, get_bonus_pay(1500))
        self.assertEqual("Invalid Argument", get_bonus_pay(2000))