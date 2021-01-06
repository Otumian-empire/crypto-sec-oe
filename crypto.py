# crypto.py
import string


class Crypto:

    def __init__(self, shift, data):
        self.shift = shift
        self.data = data
        
        self.LC_ASCII = string.ascii_lowercase
        self.STRING_SIZE = len(self.LC_ASCII)  # put 26 here

    def get_index(self, ch):
        index_ch = self.LC_ASCII.index(ch)
        index_ch += self.shift
        index_ch %= self.STRING_SIZE

        return index_ch

    def encrypt(self):
        if not self.shift:
            return self.data

        enc = ""

        for ch in self.data.lower():
            if ch in self.LC_ASCII:
                ch = self.LC_ASCII[self.get_index(ch)]

            enc += ch

        return enc

    def decrypt(self):
        self.shift = self.STRING_SIZE - self.shift

        return self.encrypt()
