# import the necessary packages
import sys
import string

def main ():
    print(atbash_cipher_v1(sys.argv[1]))


def atbash_cipher_v1(input):
    # genterate aplhabet strings forward and backward
    a_z = string.ascii_lowercase + string.ascii_uppercase
    z_a = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]

    # convert alphabet strings into lists
    a_z_list = list(a_z)
    z_a_list = list(z_a)

    # combine lists into dictionary
    atbash_dict = dict(zip(a_z_list, z_a_list))

    l = []
    for c in input:
        l.append(atbash_dict[c])

    return ''.join(l)

# figure out how to handle punctuation and spaces

if __name__ == "__main__":
    main()
