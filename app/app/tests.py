from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two number are added together"""
        self.assertEqual(add(3, 4), 7)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted and returned"""
        self.assertEqual(subtract(11, 10), 1)
