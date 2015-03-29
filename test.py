import unittest
from ScoreCalculator import singles,three_of_a_kind,four_of_a_kind,yahtzee,fullhouse,long_straight,short_straight

class TestScoreCalculator(unittest.TestCase):
	def test_ones(self):
		dice_set = [1, 2, 3, 1, 5]
		self.assertEqual(singles(dice_set,1), 2)

	def test_twos(self):
		dice_set = [2, 2, 4, 3, 2]
		self.assertEqual(singles(dice_set,2), 6)

	def test_twos(self):
		dice_set = [2, 2, 4, 3, 2]
		self.assertEqual(singles(dice_set,2), 6)

	def test_triples(self):
		dice_set = [2, 2, 5, 3, 2]
		self.assertEqual(three_of_a_kind(dice_set), 14)

		dice_set = [1, 2, 5, 3, 2]
		self.assertEqual(three_of_a_kind(dice_set), 0)

	def test_quadruples(self):
		dice_set = [2, 6, 6, 6, 6]
		self.assertEqual(four_of_a_kind(dice_set), 26)

		dice_set = [2, 6, 6, 6, 2]
		self.assertEqual(four_of_a_kind(dice_set), 0)

	def test_yahtzee(self):
		dice_set = [6, 6, 6, 6, 6]
		self.assertEqual(yahtzee(dice_set), 50)

		dice_set = [6, 6, 6, 6, 2]
		self.assertEqual(yahtzee(dice_set), 0)

	def test_fullhouse(self):
		dice_set = [1, 1, 6, 6, 6]
		self.assertEqual(fullhouse(dice_set), 25)

		dice_set = [1, 6, 6, 6, 2]
		self.assertEqual(fullhouse(dice_set), 0)

	def test_long_straight(self):
		dice_set = [2, 5, 4, 6, 3]
		self.assertEqual(long_straight(dice_set), 40)

		dice_set = [1, 1, 3, 4, 5]
		self.assertEqual(long_straight(dice_set), 0)

	def test_short_straight(self):
		dice_set = [1, 5, 4, 6, 3]
		self.assertEqual(short_straight(dice_set), 30)

		dice_set = [1, 1, 3, 4, 5]
		self.assertEqual(short_straight(dice_set), 0)

		dice_set = [6, 4, 2, 3, 5]
		self.assertEqual(short_straight(dice_set), 30)
