import unittest

from models.driver import Driver
from models.constructor import Constructor

class TestConstructor(unittest.TestCase):

    def setUp(self):
        self.driver1 = Driver("Charles Leclerc", 100, 3, 1)
        self.driver2 = Driver("Carlos Sainz", 35, 2, 0)
        self.drivers = [self.driver1, self.driver2]
        self.constructor = Constructor("Ferrari", self.driver1, self.driver2)

    def test_constructor_has_name_drivers_points(self):
        self.assertEqual("Ferrari", self.constructor.name)
        self.assertEqual([self.driver1, self.driver2], self.constructor.drivers)
        self.assertEqual(135, self.constructor.points)

    def test_constructor_can_add_points(self):
        self.driver1.add_points(25, self.constructor)
        self.driver2.add_points(18, self.constructor)

        self.assertEqual(178, self.constructor.points)

