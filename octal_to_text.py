# import the necessary packages
import sys

def main ():
    print(octal_to_text_v1(sys.argv[1]))


def octal_to_text_v1(input):
    l = input.split()
    tl = []
    for i in l:
        tl.append(chr(int(i, base=8)))
    return ''.join(tl)


if __name__ == "__main__":
    main()
