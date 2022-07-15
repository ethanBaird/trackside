import unittest
from models.drivers import Driver
from models.constructors import Constructor

class TestDriver(unittest.TestCase):

    def setUp(self):
        self.driver1 = Driver('Charles Leclerc', 100, 5, 8)
        self.driver2 = Driver("Carlos Sainz", 35, 2, 0)
        self.constructor = Constructor("Ferrari", self.driver1, self.driver2)

    def test_driver_attributes(self):
        self.assertEqual("Charles Leclerc", self.driver1.name)
        self.assertEqual(100, self.driver1.points)
        self.assertEqual(5, self.driver1.wins)
        self.assertEqual(8, self.driver1.podiums)

    def test_driver_can_add_points_wins_podiums(self):
        self.driver1.add_points(5, self.constructor)
        self.driver1.add_wins(1)
        self.driver1.add_podiums(1)

        self.assertEqual(105, self.driver1.points)
        self.assertEqual(6, self.driver1.wins)
        self.assertEqual(9, self.driver1.podiums)