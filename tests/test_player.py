import unittest
from qcapi import QCPlayer


class TestPlayerAPI(unittest.TestCase):

    def test_search(self):
        self.assertEqual(QCPlayer.exists("phy1um"), True)

    def test_get(self):
        player = QCPlayer.from_name("phy1um")
        self.assertIsInstance(player, QCPlayer)

    def test_rank(self):
        player = QCPlayer.from_name("phy1um")
        r = player.get_rank_value("duel")
        self.assertIsInstance(r, int)
