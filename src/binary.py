import sys


def main ():
    print(binary_to_text_v1(sys.argv[1]))


def binary_encode(input):
    return ' '.join(list(map(lambda x: format(ord(x),'b').zfill(8), input)))


def binary_decode(input):
    return ''.join(list(map(lambda x: chr(int(x, base=2)), input.split())))


if __name__ == "__main__":
    main()
