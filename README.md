
# Requirements : 
1. python3.8

# Installation : 
1. virtualenv env
2. pip install -r requirements.txt

# Example usage  :

1. **Initialization of the key exchange**
    ```
    - python alice.py dhke -p 23 -g 5
    - 23 OK (This is a prime number .)
    - 5 is a prime root of 23
    - Alice private key : 160
    - Alice public key : 8
    ```

    ```
    - python bob.py dhke -p 23 -g 5
    - 23 OK (This is a prime number .)
    - 5 is a prime root of 12
    - Bob private key : 12
    - Bob public key : 18
    ```

2. **Finalization of the key exchange**


    ```
    - python alice.py dhke -a 160 -B 18 -p 23
    - Key : 8
    ```

    ```
    - python bob.py dhke -A 8 -b 12 -p 23
    - Key : 8
    ```

3. **Encryption and decryption of a single message**

    ```
    - python alice.py des -p 'This is the secret message.' -k 18
    - Raw cipher :  b'\x9dQ\xb0"g\x05\xce\x0f\xc7\x1c\x0f\xaan\xeb\xf8\xfd\xf3j\'\xdf\xb5\xa8\xddc\xb3K)\xfa)=\xab\xa8'
    - Readable cipher :  nVGwImcFzg/HHA+qbuv4/fNqJ9+1qN1js0sp+ik9q6g=
    ```

    ```
    - python bob.py des -k 18 -c 'nVGwImcFzg/HHA+qbuv4/fNqJ9+1qN1js0sp+ik9q6g='
    - This is the secret message.
    ```
