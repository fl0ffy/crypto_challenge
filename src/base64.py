# import the necessary packages
import sys
import base64

def main ():
    print(base64_to_ascii_v1(sys.argv[1]))


def base64_encode(input):
    pass


def base64_decode(input):
    return base64.b64decode(input).decode('ascii')


if __name__ == "__main__":
    main()
