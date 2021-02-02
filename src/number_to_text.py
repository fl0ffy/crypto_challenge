import sys
import string

def main ():
    print(number_to_text_v1(sys.argv[1]))


# number to letter 1 to 1
def number_to_text_v1(input):
    alpha_string = string.ascii_lowercase
    l = input.split()
    tl = []
    for i in l:
        itl = []
        for c in i.split('-'):
            itl.append(alpha_string[int(c)-1])
        tl.append(''.join(itl))
    return ' '.join(tl)


if __name__ == "__main__":
    main()
