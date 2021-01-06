# test.py
from crypto import Crypto
import unittest


class TestCrypto(unittest.TestCase):

    def test_encrypt_a_is_b_in_one_shift(self):
        enc = Crypto(1, "a")

        self.assertEqual(enc.encrypt(), "b")

    def test_encrypt_z_is_b_in_two_shift(self):
        enc = Crypto(2, "z")

        self.assertEqual(enc.encrypt(), "b")

    def test_encrypt_hello_is_jgnnq_in_two_shift(self):
        enc = Crypto(2, "hello")

        self.assertEqual(enc.encrypt(), "jgnnq")

    def test_decrypt_b_is_a_in_one_shift(self):
        enc = Crypto(1, "b")

        self.assertEqual(enc.decrypt(), "a")

    def test_decrypt_b_is_z_in_two_shift(self):
        enc = Crypto(2, "b")

        self.assertEqual(enc.decrypt(), "z")

    def test_decrypt_jgnnq_is_hello_in_two_shift(self):
        enc = Crypto(2, "jgnnq")

        self.assertEqual(enc.decrypt(), "hello")


if __name__ == '__main__':
    unittest.main()
