import unittest
from Wallet import Wallet
from WalletManager import WalletManager

class TestWallet(unittest.TestCase):

    def setUp(self):
        # Runs before each test
        self.wallet = Wallet("Alice")

    def test_add_money_positive(self):
        self.wallet.add_money(100)
        self.assertEqual(self.wallet.balance, 100)
        self.assertIn("Added 100", self.wallet.history[0])

    def test_add_money_negative(self):
        self.wallet.add_money(-50)
        self.assertEqual(self.wallet.balance, 0)  

if __name__ == "__main__":
    unittest.main(verbosity=2)