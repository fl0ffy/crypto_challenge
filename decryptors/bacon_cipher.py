# import the necessary packages
import sys
from more_itertools import sliced

#make sure to install more_itertools

def main ():
    print(bacon_cipher_v1(sys.argv[1]))

# make lookup with upper and lower
# add checks for spaces
def bacon_cipher_v1(input):

    lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
            'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
            'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
            'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
            'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}

    inverse_lookup = {v: k for k, v in lookup.items()}

    clean_input = ''.join(input.split()).lower()
    l = list(sliced(clean_input, 5))
    tl = []
    for i in l:
        tl.append(inverse_lookup[i])

    return ''.join(tl).lower()


if __name__ == "__main__":
    main()
