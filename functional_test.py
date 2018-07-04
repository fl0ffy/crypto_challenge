from atbash import atbash_cipher_v1
#import base64_to_ascii
#import caesar_cipher
#import hex_to_ascii
#import binary_to_text

def main():
    # atbash
    atbash_ciphertext = 'Gzxl'
    atbash_plaintext = atbash_cipher_v1(atbash_ciphertext)
    print('---------- Atbash Test ------------')
    print('ciphertext: %s'.format(atbash_ciphertext))
    print('deciphered plaintext: %s'.fomrat(atbash_plaintext))

    # base64
    # caesar
    # hex
    # binary


if __name__ == "__main__":
    main()
