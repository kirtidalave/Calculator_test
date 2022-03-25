from unittest import result

import calculator

import unittest

class TestCalculator (unittest. TestCase):

    def test_add(self):
        x=10
        y=20
        result=calculator.add(x, y)
        self.assertEqual (result, x+y)

    def test_add(self):
        x=10
        y=20
        result=calculator.add(x, y)
        self.assertEqual (result, x+y)
