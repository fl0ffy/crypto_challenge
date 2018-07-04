# import the necessary packages
import sys

def main ():
    print(hex_to_ascii_v1(sys.argv[1]))


def hex_to_ascii_v1 (input):
    return bytearray.fromhex(''.join(input.split())).decode()


if __name__ == "__main__":
    main()
