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

    def test_str(self):
        self.assertIs(print(self.cart), None)
        assert len(self.cart) == 29

    def test_isempty(self):
        self.assertFalse(self.cart.is_empty(), False)

    def test_contains(self):
        self.assertIn('#', str(self.cart))


class TestNpc(unittest.TestCase):
    def setUp(self):
        self.npc = Npc()

    def test_init(self):
        self.assertIsNotNone(self.npc.cart)
        self.assertIsNotNone(self.npc.name)

    def test_step(self):
        self.assertTrue(self.npc.step(50), True)
        self.assertTrue(self.npc.step(10), True)
