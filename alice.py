import sys
import random
from math import gcd
from Crypto.Cipher import DES
from base64 import b64encode, b64decode


def pad(text):
    n = len(text) % 8
    if n:
        n = 8 - n
    return text + (b' ' * n)


def check_prime(number):
    num = int(number)
    not_prime = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                not_prime = True
                break
    if not_prime:
        print(num, "is not a prime number.")
        sys.exit()

    print(num, "OK (This is a prime number .)")


def prime_roots(modulo):
    prime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if prime_set == {pow(g, powers, modulo) for powers in range(1, modulo)}]


def check_prime_root(p, g):
    prim_root_list = prime_roots(p)
    if g in prim_root_list:
        print(g, "is a prime root of", p)
    else:
        print(g, "is not a prime root of", p)
        sys.exit()


if __name__ == "__main__":

    if sys.argv[1] == "dhke":

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

        if "-p" in sys.argv:

            key = pad(
                bytes(sys.argv[sys.argv.index("-k") + 1].encode("utf-8")))

            plaintext = pad(
                bytes(sys.argv[sys.argv.index("-p") + 1].encode("utf-8")))

            des = DES.new(key, mode=DES.MODE_ECB)

            print("Raw cipher : ", des.encrypt(pad(plaintext)))

            readable_cipher = b64encode(
                des.encrypt(pad(plaintext))).decode("utf-8")

            print("Readable cipher : ", readable_cipher)

            # print(des.decrypt(b64decode(readable_cipher)).decode("utf-8").strip())

        elif "-c" in sys.argv:

            key = pad(
                bytes(sys.argv[sys.argv.index("-k") + 1].encode("utf-8")))

            cipher = pad(
                bytes(sys.argv[sys.argv.index("-c") + 1].encode("utf-8")))

            des = DES.new(key, mode=DES.MODE_ECB)

            print(des.decrypt(b64decode(cipher)).decode("utf-8").strip())

    else:
        print("Missing command.")
        sys.exit()
