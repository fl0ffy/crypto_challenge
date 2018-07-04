# import the necessary packages
import sys
import codecs

def main ():
    print(caesar_cipher_v2(sys.argv[1]))

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

if __name__ == "__main__":
    main()
