import unittest
from Wallet import Wallet
from WalletManager import WalletManager

class TestWallet(unittest.TestCase):

    def setUp(self):
        self.password = "abcdefgh"
        self.name = "alice"
        self.loggedIn = True
        # Runs before each test
        self.wallet = Wallet("alice","abcdefgh")
        self.wallet.authenticate(self.name,self.password)

     # test authentication

    def test_authentication_success(self):
        self.wallet.authenticate("alice","abcdefgh")
        result = self.wallet.authenticate("alice","abcdefgh")
        self.assertTrue(result)

    def test_authentication_failure(self):
        result = self.wallet.authenticate("alice","abcdefg")
        self.assertFalse(result)


    # test checking balance

    def test_check_balance_true(self):
        self.wallet.balance=0
        self.wallet.check_balance()
        self.assertEqual(self.wallet.balance,0)
        self.assertTrue(self.wallet.loggedin)

    def test_check_balance_authentication(self):
        self.wallet.loggedin = False
        self.wallet.check_balance()
        self.assertEqual(self.wallet.balance, 0)
        self.wallet.authenticate("alice","abcdefg")
        self.assertFalse(self.wallet.loggedin)

    # testing adding money

    def test_add_money_positive(self):
        self.wallet.add_money(100)
        self.assertEqual(self.wallet.balance, 100)
        self.assertIn("Added 100", self.wallet.history[0])
        self.assertTrue(self.wallet.loggedin)

    def test_add_money_negative(self):
        self.wallet.add_money(-50)
        self.assertEqual(self.wallet.balance, 0)
        self.assertTrue(self.wallet.loggedin)  

    # testing spending money

    def test_spend_money_positive(self):
        self.wallet.balance=200
        self.wallet.spend_money(100)
        self.assertEqual(self.wallet.balance, 100)
        self.assertIn("Spent 100", self.wallet.history[0])
        self.assertTrue(self.wallet.loggedin)

    def test_spend_money_negative(self):
        self.wallet.spend_money(-50)
        self.assertEqual(self.wallet.balance, 0)
        self.assertTrue(self.wallet.loggedin) 

    def  test_spend_money_more_than_balance(self):
        self.wallet.spend_money(50)
        self.assertEqual(self.wallet.balance, 0)
        self.assertTrue(self.wallet.loggedin) 

    # receiving money tests

    def test_receive_money_positive(self):
        self.wallet.balance=200
        self.wallet.receive_money(100, "Bob")
        self.assertEqual(self.wallet.balance, 300)
        self.assertIn(f"Received 100 from Bob", self.wallet.history[0])
        self.assertTrue(self.wallet.loggedin)

    def test_receive_money_negative(self):
        self.wallet.balance=200
        self.wallet.receive_money(-100, "Bob")
        self.assertEqual(self.wallet.balance, 200)
        self.assertTrue(self.wallet.loggedin)

    def test_receive_money_zero(self):
        self.wallet.balance=200
        self.wallet.receive_money(0, "Bob")
        self.assertEqual(self.wallet.balance, 200)
        self.assertTrue(self.wallet.loggedin)

    
    # testing transferring

    def test_transfer_money_positive(self):
        self.wallet.balance=200
        receiver=Wallet("Bob","abc")
        self.wallet.transfer_money(100, receiver)
        self.assertEqual(self.wallet.balance, 100)
        self.assertIn("Transferred 100 to Bob", self.wallet.history[0])
        self.assertTrue(self.wallet.loggedin)

    def test_transfer_money_negative(self):
        
        self.wallet.balance=200
        receiver=Wallet("Bob","abc")
        self.wallet.transfer_money(-100, receiver)
        self.assertEqual(self.wallet.balance, 200)
        self.assertTrue(self.wallet.loggedin)

    def test_transfer_money_zero(self):
        self.wallet.balance=200
        receiver=Wallet("Bob","abc")
        self.wallet.transfer_money(0, receiver)
        self.assertEqual(self.wallet.balance, 200)
        self.assertTrue(self.wallet.loggedin)

    def test_transfer_money_insufficient_balance(self):
        self.wallet.balance=200
        receiver=Wallet("Bob","abc")
        self.wallet.transfer_money(300, receiver)
        self.assertEqual(self.wallet.balance, 200)
        self.assertTrue(self.wallet.loggedin)

    def test_transfer_money_to_own_account(self):
        self.wallet.balance=200
        receiver=self.wallet
        self.wallet.transfer_money(300, receiver)
        self.assertEqual(self.wallet.balance, 200)
        self.assertTrue(self.wallet.loggedin)

    #view transaction history tests

    def test_transaction_history(self):
        self.wallet.balance=200
        receiver=Wallet("Bob","abc")
        self.wallet.transfer_money(100,receiver)
        self.assertEqual(self.wallet.balance, 100)
        self.assertIn("Transferred 100 to Bob", self.wallet.history[0])
        self.assertTrue(self.wallet.loggedin)

    def test_transaction_history_empty(self):
        self.wallet.balance=200
        self.assertEqual(self.wallet.history,[])
        self.assertTrue(self.wallet.loggedin)

if __name__ == "__main__":
    unittest.main(verbosity=2)