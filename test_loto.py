import unittest

import pytest
from loto import Game, Person, Npc, Cart


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_init(self):
        self.assertTrue(self.cart.cart, True)

    def test_create(self):
        self.assertTrue(len(self.cart.cart), 27)

    def test_dec(self):
        self.assertIsNotNone(self.cart.dec())

    def test_showCart(self):
        self.assertTrue(self.cart.show_cart(), True)

    def test_isempty(self):
        self.assertFalse(self.cart.is_empty(), False)


class TestNpc(unittest.TestCase):
    def setUp(self):
        self.npc = Npc()

    def test_init(self):
        self.assertIsNotNone(self.npc.cart)
        self.assertIsNotNone(self.npc.name)

    def test_step(self):
        self.assertTrue(self.npc.step(50), True)
        self.assertTrue(self.npc.step(10), True)

# class TestGame():
#     def setUp(self):
#         self.game = Game()
#
#     def test_init(self):
#         game = Game()
#         assert len(game.bag)==100
#         # with pytest.raises(Exception):
#         #     self.game.bag
