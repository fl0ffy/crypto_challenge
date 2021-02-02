import pytest
from src.base64 import *

plaintext ="TG9vayBhYm92ZSBhbmQgeW91IHdpbGwgc2VlIGEgdGVlbnkgdGlueSBnb2xkZW4ga2V5Cg=="
ciphertext ="Look above and you will see a teeny tiny golden key"


def test_base64_encode():
    assert base64_encode(plaintext) == ciphertext


def test_base64_decode():
    assert base64_decode(ciphertext) == plaintext
