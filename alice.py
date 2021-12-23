import sys
import random
from math import gcd
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def check_prime(number):

    num = int(number)

    # To take input from the user
    #num = int(input("Enter a number: "))

    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number.")
        sys.exit()

    print(num, "OK (This is a prime number .)")


def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo) for powers in range(1, modulo)}]


def check_prime_root(p, g):
    prim_root_list = primRoots(p)

    # print(prim_root_list)

    if g in prim_root_list:
        print(g, "is a prime root of", p)
    else:
        print(g, "is not a prime root of", p)
        sys.exit()


if sys.argv[1] == "dhke":
    #print("dhke mode")
    if "-p" not in sys.argv:
        print("Example usage : alice.py dhke -p 23 -g 5")
        sys.exit()

    if "-g" in sys.argv:

        p = int(sys.argv[sys.argv.index("-p") + 1])

        g = int(sys.argv[sys.argv.index("-g") + 1])

        check_prime(p)

        check_prime_root(p, g)

        private_key = random.randint(1, 200)

        public_key = pow(g, private_key, p)

        print("Private key :", private_key, "\nPublic : ", public_key)

    elif "-a" in sys.argv and "-B" in sys.argv:
        p = int(sys.argv[sys.argv.index("-p") + 1])

        alice_private = int(sys.argv[sys.argv.index("-a") + 1])

        bob_public = int(sys.argv[sys.argv.index("-B") + 1])

        print("Key : ", pow(bob_public, alice_private, p))


elif sys.argv[1] == "des":

    #p = int(sys.argv[sys.argv.index("-p") + 1])

    k = (18).to_bytes(DES.key_size, byteorder='little')

    cipher = DES.new(key=k, mode=DES.MODE_ECB)

    plaintext =  b'This is the secret message.'

    
    msg = cipher.encrypt(pad(bytes(plaintext), DES.block_size))

    print(b"\xd55\xc3d\x9d\xf4\x11y\x10\\\x81\xd1\x88n\xdc\xc2\xbb\xed2R\x81'\x8a\xf4\x91g\x90\x18\xa49\\\xbd")
    print(msg)


else:
    print("quitting")
    sys.exit()
