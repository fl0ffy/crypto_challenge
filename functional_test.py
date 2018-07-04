from atbash import atbash_cipher_v1
from base64_to_ascii import base64_to_ascii_v1
from caesar_cipher import caesar_cipher_v2
from hex_to_ascii import hex_to_ascii_v1
from binary_to_text import binary_to_text_v1
from bacon_cipher import bacon_cipher_v1

def main():
    print()

    # atbash
    atbash_ciphertext = 'Blfdrooivzoobdrhsgszgblfxslhvgsvurhs'
    atbash_plaintext = atbash_cipher_v1(atbash_ciphertext)
    print('---------- Atbash Test ------------')
    print('ciphertext: ' + atbash_ciphertext)
    print('deciphered plaintext: ' + atbash_plaintext)
    print()
    #print('ciphertext: %s'.format(atbash_ciphertext))
    #print('deciphered plaintext: %s'.format(atbash_plaintext))

    # base64
    base64_ciphertext = 'TG9vayBhYm92ZSBhbmQgeW91IHdpbGwgc2VIIGEgdGVIbnkgdGIueSBnb2xkZW4ga2V5Cg=='
    base64_plaintext = base64_to_ascii_v1(base64_ciphertext)
    print('---------- Base64 Test ------------')
    print('ciphertext: ' + base64_ciphertext)
    print('deciphered plaintext: ' + base64_plaintext)
    print()

    # caesar
    caesar_ciphertext = 'gur gernfher yvrf gb gur jrfg'
    caesar_plaintext = caesar_cipher_v2(caesar_ciphertext)
    print('---------- Caesar Test ------------')
    print('ciphertext: ' + caesar_ciphertext)
    print('deciphered plaintext: ' + caesar_plaintext)
    print()

    # hex
    hex_ciphertext = '''49 66 20 74 72 65 61 73 75 72 65 20 69 73 20 77 68 61 74 20 79 6f 75 20 73 65
    65 6b 2c 20 61 73 6b 20 66 6f 72 20 68 65 6c 70 20 66 72 6f 6d 20 79 6f 75 72 20
    66 72 69 65 6e 64 20 77 69 74 68 20 74 68 65 20 62 65 61 6b 0a'''
    hex_plaintext = hex_to_ascii_v1(hex_ciphertext)
    print('---------- Hex Test ------------')
    print('ciphertext: ' + hex_ciphertext)
    print('deciphered plaintext: ' + hex_plaintext)
    print()

    # binary
    binary_ciphertext = '''01101001 01100110 00100000 01111001 01101111 01110101 00100000
    01110000 01110101 01110011 01101000 00100000 01101111 01101110
    00100000 01110100 01101000 01100101 00100000 01110011 01101110
    01100001 01101011 01100101 00100000 01111001 01101111 01110101
    01110010 00100000 01100010 01101111 01101110 01100101 01110011
    00100000 01110100 01101000 01100101 01111001 00100000 01110111
    01101001 01101100 01101100 00100000 01100010 01110010 01100101
    01100001 01101011 0001010'''
    binary_plaintext = binary_to_text_v1(binary_ciphertext)
    print('---------- Binary Test ------------')
    print('ciphertext: ' + binary_ciphertext)
    print('deciphered plaintext: ' + binary_plaintext)
    print()

    #bacon
    bacon_ciphertext = '''
    AAABAABBBAABBABAABBABAAABAAAAABAABBBABAAABABBAAAAABAA
    BBABAAAABBBAABBABBAABA BBAAAABBBABABAA
    AABBBAAAAABABABAABAA AABABABBBABABAAABBABAAABB
    BAABBAABBBAABAA
    BAABBBAAABAABAAAAAAABAABABABAABAAABAABAA ABBBAAABAB
    BAABBAABBBAABAA BAABAABAAAABABBBABABAABAABAAAB
    BAABABAABBAAAAABAAAB AAAABBAAABABAAAABBABAABBA
    BAABBAABBBABAAABAABA AAABAABBBAAAABBAABAA
    BABBAABBBABAAABAAABB BAABBABBBA
    ABAABAABAAABBABABBABBBAAA ABBBABAAAB
    BAABBAABAABAABABAABA BAABBABBBA AABBAAABAABAABB
    BBAAAABBBABABAABAAAB ABBBBBAAABABAAABBAABAABAA
    AABBABABAAAAABAAAABAABAAA
    '''
    bacon_plaintext = bacon_cipher_v1(bacon_ciphertext)
    print('---------- Binary Test ------------')
    print('ciphertext: ' + bacon_ciphertext)
    print('deciphered plaintext: ' + bacon_plaintext)
    print()

if __name__ == "__main__":
    main()
