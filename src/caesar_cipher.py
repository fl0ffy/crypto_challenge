# import the necessary packages
import sys
import codecs   # For v2
import string   # For v3

def main ():
    #print(caesar_cipher_v1(sys.argv[1]))
    #print(caesar_cipher_v2(sys.argv[1]))
    print(caesar_cipher_v3(sys.argv[1],13))


# default rot13
# add ability to change key and set default as 13
# add checks for spaces
# force lowercase matching
def caesar_cipher_v1 (input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    compared = alphabet * 2
    key = 13
    plain_text = []
    for letter in input_string:
        new_letter = compared.index(letter) + 13
        plain_text.append(compared[new_letter])
    return ''.join(plain_text)


def caesar_cipher_v2(input):
    return codecs.decode(input, 'rot_13')


def caesar_cipher_v3(input,key):
    SYMBOLS_UPPER = string.ascii_uppercase
    SYMBOLS_LOWER = string.ascii_lowercase

    plaintext = []

    for c in input:
        if c.isupper():
            symbols = SYMBOLS_UPPER
        elif c.islower():
            symbols = SYMBOLS_LOWER
        else:
            plaintext.append(c)
            continue

        ciphertext_index = symbols.index(c)

        # handle wrap around
        plaintext_index = int(ciphertext_index) + int(key)

        while plaintext_index > len(symbols):
            plaintext_index -= len(symbols)

        plaintext.append(symbols[plaintext_index])

    return ''.join(plaintext)


if __name__ == "__main__":
    main()
