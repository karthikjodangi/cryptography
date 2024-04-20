import os
import sys

def rotate_left(num, shift):
    num &= 0b1111111
    res = ((num << shift) | (num >> (7 - shift))) & 0b1111111
    return chr(res)

def rotate_right(num, shift):
    num &= 0b1111111
    res = ((num >> shift) | (num << (7 - shift))) & 0b1111111
    return chr(res)

def main():
    n = len(sys.argv)
    password = sys.argv[3]

    if n != 6:
        print("Incorrect no. of arguments passed.")
        exit()

    if not password.isdigit():
        print("password must contain only digits (0-9)")
        exit()

    pl = len(password)

    if not os.path.exists(sys.argv[4]):
        print("given input file not found")
        exit()

    if sys.argv[1] == "encrypt":
        if sys.argv[2] == "xrot":
            f1 = open(sys.argv[4], "r")
            ip = f1.read()
            result = ''

            for i in range(len(ip)):
                if (ord(password[i % pl]) - 48) > 6:
                    pa = (ord(password[i % pl]) - 48) % 7
                else:
                    pa = ord(password[i % pl]) - 48
                result += rotate_left(ord(ip[i]), pa)

            f2 = open(sys.argv[5], "w")
            f2.write(result)
            f1.close()
            f2.close()
            print("Encrypted successfully using xrot algorithm")
        elif sys.argv[2] == "xplus":
            f1 = open(sys.argv[4], "r")
            ip = f1.read()
            result = ''

            for i in range(len(ip)):
                pa = ord(password[i % pl]) - 48
                val = ord(ip[i]) + (i + 1) * pa

                if val > 127:
                    val = val % 127
                result += chr(val)

            f2 = open(sys.argv[5], "w")
            f2.write(result)
            f1.close()
            f2.close()
            print("Encrypted successfully using xplus algorithm")
        else:
            print("Incorrect Algorithm, choose between xrot/xplus")
            exit()
    elif sys.argv[1] == "decrypt":
        if sys.argv[2] == "xrot":
            f1 = open(sys.argv[4], "r")
            ip = f1.read()
            result = ''

            for i in range(len(ip)):
                if (ord(password[i % pl]) - 48) > 6:
                    pa = (ord(password[i % pl]) - 48) % 7
                else:
                    pa = ord(password[i % pl]) - 48
                    
                result += rotate_right(ord(ip[i]), pa)

            f2 = open(sys.argv[5], "w")
            f2.write(result)
            f1.close()
            f2.close()
            print("Decrypted successfully using xrot algorithm")
        elif sys.argv[2] == "xplus":
            f1 = open(sys.argv[4], "r")
            ip = f1.read()
            f2 = open(sys.argv[5], "w")
            
            for i in range(len(ip)):
                pa = ord(password[i % pl]) - 48
                if ip[i] == '\n':
                    val = 13 - (((i + 1) * pa) % 127)
                else:
                    val = ord(ip[i]) - (((i + 1) * pa) % 127)

                if val <= 0:
                    val = 127 + val
                f2.write(chr(val))
            f1.close()
            f2.close()
            print("Decrypted successfully using xplus algorithm")
        else:
            print("Incorrect Algorithm, choose between xrot/xplus")
            exit()
    else:
        print("Incorrect argument, choose between encrypt/decrypt")
        exit()

    f1 = open(sys.argv[4], "r")
    ip = f1.read()
    print(f"Input file length: {len(ip)}")
    f1.close()
    f2 = open(sys.argv[5], "r")
    op = f2.read()
    print(f"Output file length: {len(op)}")
    f2.close()

if __name__ == "__main__":
    main()
