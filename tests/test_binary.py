import pytest
from src.binary import *

plaintext ='''01101001 01100110 00100000 01111001 01101111 01110101 00100000
01110000 01110101 01110011 01101000 00100000 01101111 01101110
00100000 01110100 01101000 01100101 00100000 01110011 01101110
01100001 01101011 01100101 00100000 01111001 01101111 01110101
01110010 00100000 01100010 01101111 01101110 01100101 01110011
00100000 01110100 01101000 01100101 01111001 00100000 01110111
01101001 01101100 01101100 00100000 01100010 01110010 01100101
01100001 01101011 0001010'''
ciphertext ="if you push on the snake your bones they will break\n"


def test_binary_encode():
    assert binary_encode(plaintext) == ciphertext


def test_binary_decode():
    assert binary_decode(ciphertext) == plaintext