import sys
import string


# def main ():
#     print(atbash_encode(sys.argv[1]))


def atbash_cipher_encode(input):
    l = []
    m = 26
    for char in input:
        if char.isalpha():
            if char.isupper():
                n = 64
            else:
                n = 96
            l.append( chr((( -(ord(char) - n) % m) + 1) + n) )
        else:
            l.append(char)
    return ''.join(l)


def atbash_cipher_decode(input):
    return (atbash_cipher_encode(input))


# if __name__ == "__main__":
#     main()
