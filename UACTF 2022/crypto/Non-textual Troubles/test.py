from random import seed, randrange

seed(True, version=2)

with open("ciphertext.txt", "r") as read, open("plaintext.txt", "w") as write:
    ciphertext = read.read()

    for char in ciphertext:
        A = ord(char)
        B = randrange(256)
        plaintext = chr(A ^ B)
        write.write(plaintext)