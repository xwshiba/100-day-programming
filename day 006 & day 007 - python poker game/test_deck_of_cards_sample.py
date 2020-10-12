import unittest
from deck_of_cards import Card, Deck

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card('A', 'Hearts')

	def test_init(self):
		"""card init should be correct"""
		self.assertEqual(self.card.suit, 'Hearts')
		self.assertEqual(self.card.value, 'A')

	def test_repr(self):
		"""repr of test should be correct"""
		self.assertEqual(repr(self.card), 'A of Hearts')

class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		"""deck init should match 52"""
		self.assertTrue(isinstance(self.deck.cards, list))
		self.assertEqual(len(self.deck.cards), 52)

if __name__ =="__main__":
	unittest.main()