import sys
import random
from math import gcd

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
        print(num, "is not a prime number")
        sys.exit()

    print(num, "is a prime number")


def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo) for powers in range(1, modulo)}]


def check_prime_root(p,g):
    prim_root_list = primRoots(p)

    if g in prim_root_list :
        print(g, "is a prime root of", p)
    else :
        print(g, "is not a prime root of", p)
        sys.exit()

if sys.argv[1] == "dhke":
    #print("dhke mode")
    if "-p" not in sys.argv or "-g" not in sys.argv:
        print("Example usage : alice.py dhke -p 23 -g 5")
        sys.exit()

    
    p = int(sys.argv[sys.argv.index("-p") + 1])

    g = int(sys.argv[sys.argv.index("-g") + 1])

    check_prime(p)

    check_prime_root(p,g)

    private_key = random.randint(1,200)

    public_key = pow(g,private_key,p)



    print("Private key :", private_key, "\nPublic : ",public_key)
    
    """
    
    alice private : 50
    alice public : 1
    bob private : 129
    bob public : 2

    """

    print(pow(2,50,11))

    print(pow(1,129,11))


elif sys.argv[1] == "des":
    print("des mode")
else:
    print("quitting")
    sys.exit()
