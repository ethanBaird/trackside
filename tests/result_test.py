import unittest

from models.result import Result
from models.score import Score

class TestResult(unittest.TestCase):

    def setUp(self):
        self.result = Result(1, True, True)

    def test_result_has_attributes(self):
        self.assertEqual(1, self.result.position)
        self.assertEqual(True, self.result.win)
        self.assertEqual(True, self.result.podium)

    def test_result_can_get_score(self):
        pass

