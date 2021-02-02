from atbash import atbash_cipher_v1
from base64_to_ascii import base64_to_ascii_v1
from caesar_cipher import caesar_cipher_v2
from hex_to_ascii import hex_to_ascii_v1
from binary_to_text import binary_to_text_v1
from bacon_cipher import bacon_cipher_v1
from octal_to_text import octal_to_text_v1
from number_to_text import number_to_text_v1

def main():
    print()

    # atbash
    atbash_ciphertext = 'Blfdrooivzoobdrhsgszgblfxslhvgsvurhs'
    atbash_plaintext = atbash_cipher_v1(atbash_ciphertext)
    print('---------- Atbash Test ------------')
    print('ciphertext: %s' %  atbash_ciphertext)
    print('deciphered plaintext: %s' % atbash_plaintext)
    print()
    #print('ciphertext: %s'.format(atbash_ciphertext))
    #print('deciphered plaintext: %s'.format(atbash_plaintext))

    # base64
    base64_ciphertext = 'TG9vayBhYm92ZSBhbmQgeW91IHdpbGwgc2VIIGEgdGVIbnkgdGIueSBnb2xkZW4ga2V5Cg=='
    base64_plaintext = base64_to_ascii_v1(base64_ciphertext)
    print('---------- Base64 Test ------------')
    print('ciphertext: %s' % base64_ciphertext)
    print('deciphered plaintext: %s' % base64_plaintext)
    print()

    # caesar
    caesar_ciphertext = 'gur gernfher yvrf gb gur jrfg'
    caesar_plaintext = caesar_cipher_v2(caesar_ciphertext)
    print('---------- Caesar Test ------------')
    print('ciphertext: %s' % caesar_ciphertext)
    print('deciphered plaintext: %s' % caesar_plaintext)
    print()

    # hex
    hex_ciphertext = '''49 66 20 74 72 65 61 73 75 72 65 20 69 73 20 77 68 61 74 20 79 6f 75 20 73 65
    65 6b 2c 20 61 73 6b 20 66 6f 72 20 68 65 6c 70 20 66 72 6f 6d 20 79 6f 75 72 20
    66 72 69 65 6e 64 20 77 69 74 68 20 74 68 65 20 62 65 61 6b 0a'''
    hex_plaintext = hex_to_ascii_v1(hex_ciphertext)
    print('---------- Hex Test ------------')
    print('ciphertext: %s' % hex_ciphertext)
    print('deciphered plaintext: %s' % hex_plaintext)
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
    print('ciphertext: %s' % binary_ciphertext)
    print('deciphered plaintext: %s' % binary_plaintext)
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
    print('ciphertext: %s' % bacon_ciphertext)
    print('deciphered plaintext: %s' % bacon_plaintext)
    print()

    #octal
    octal_ciphertext = '''
    124 150 145 040 164 162 145 141 163 165 162 145 040 154 151 145 163 040
    164 157 040 164 150 145 040 163 157 165 164 150 040 151 156 040 164 150
    145 040 103 141 166 145 163 040 157 146 040 115 141 154 145 146 151 143
    165 163 015 012
    '''
    octal_plaintext = octal_to_text_v1(octal_ciphertext)
    print('---------- Octal Test ------------')
    print('ciphertext: %s' % octal_ciphertext)
    print('deciphered plaintext: %s' % octal_plaintext)
    print()

    #number
    number_ciphertext = '''
    25-15-21 3-15-14-20-9-14-21-5 1-14-4 4-5-3-9-4-5 20-15 20-1-11-5 20-8-5
    13-15-21-14-20-1-9-14 16-1-19-19 20-15 20-8-5 19-15-21-20-8 1-6-20-5-18
    19-5-22-5-18-1-12 8-15-21-18-19 25-15-21 5-14-3-15-21-14-20-5-18
    1 3-21-18-9-15-21-19 19-5-20 15-6 3-12-9-6-6-19 2-12-15-3-11-9-14-7
    25-15-21-18 23-1-25 1-6-20-5-18 19-3-1-12-9-14-7 20-8-5 6-1-3-5 15-6
    20-8-5 3-12-9-6-6 25-15-21 5-14-3-15-21-14-20-5-18 1 12-1-18-7-5 19-9-12-22-5-18
    19-20-1-20-21-5 4-5-16-9-3-20-9-14-7 1-14 1-14-3-9-5-14-20
    7-15-4 9-20 9-19 17-21-9-20-5 15-12-4 1-14-4 3-15-22-5-18-5-4 23-9-20-8
    4-21-19-20 2-21-20 9-20 1-16-16-5-1-18-19 20-15 8-1-22-5 18-1-20-8-5-18
    12-1-18-7-5 1-14-4 16-18-9-3-5-12-5-19-19 10-5-23-5-12-19 6-15-18
    5-25-5-19 20-8-9-19 13-21-19-20 2-5 20-8-5 20-18-5-1-19-21-18-5 15-6 20-8-5
    19-9-12-22-5-18 19-20-1-18

    25-15-21 4-5-3-9-4-5 20-15 21-19-5 25-15-21-18 11-14-9-6-5 20-15 18-5-13-15-22-5
    20-8-5 10-5-23-5-12-19 19-15 25-15-21 3-1-14 18-5-20-21-18-14
    20-15 20-8-5 19-8-9-16 20-15 19-8-15-23 3-1-16-20-1-9-14 17-21-9-3-11-19-1-14-4
    1-14-4 7-1-20-8-5-18 19-15-13-5 15-6 20-8-5 3-18-5-23
    20-15 18-5-20-21-18-14 20-15 8-5-12-16 3-1-18-18-25 20-8-5 19-20-1-20-21-5
    1-19 20-8-5 19-9-12-22-5-18 9-19 1-12-19-15 22-1-12-21-1-2-12-5
    20-21-18-14 20-15 16-1-7-5 5-9-7-8-20-5-5-14

    25-15-21 14-15-20-9-3-5 1-14 9-14-19-3-18-9-16-20-9-15-14 18-21-14-14-9-14-7
    20-8-5 12-5-14-7-20-8 15-6 20-8-5 2-1-19-5 15-6 20-8-5 19-20-1-20-21-5
    9-20 1-16-16-5-1-18-19 20-15 2-5 1 16-18-1-25-5-18 1-14-4
    25-15-21 18-5-1-4 20-8-5 6-15-12-12-15-23-9-14-7 23-15-18-4-19 15-21-20
    12-15-21-4 7-15-4 15-6 20-8-5 19-9-12-22-5-18 19-20-1-18 19-8-9-14-5
    25-15-21-18 12-9-7-8-20 21-16-15-14 13-25 16-1-20-8 1-19-20-18-21-13
    1-18-7-5-14-20-9-21-13 20-21-18-14 20-15 16-1-7-5 14-9-14-5
    '''
    number_plaintext = number_to_text_v1(number_ciphertext)
    print('---------- Octal Test ------------')
    print('ciphertext: %s' % number_ciphertext)
    print('deciphered plaintext: %s' % number_plaintext)
    print()



if __name__ == "__main__":
    main()
