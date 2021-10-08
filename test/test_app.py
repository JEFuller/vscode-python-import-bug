import unittest

from app import app

class Test_Foo(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1)