import pytest
from src.atbash_cipher import *

plaintext = "Youwillreallywishthatyouchosethefish"
ciphertext ="Blfdrooivzoobdrhsgszgblfxslhvgsvurhs"


def test_atbash_cipher_encode():
    assert atbash_cipher_encode(plaintext) == ciphertext


def test_atbash_cipher_decode():
    assert atbash_cipher_decode(ciphertext) == plaintext
