import sys
from unittest import TestCase
class Evaluate(TestCase):

    @property
    def test_odd_number(num):
        if num % 2 == 0:
            return "This is an even number."
        else:
            return "This is an odd number."
