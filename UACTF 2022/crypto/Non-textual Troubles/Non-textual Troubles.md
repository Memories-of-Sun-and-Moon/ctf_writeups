# Non-textual Troubles

## 問題（要約）

ciphertext と 暗号化するプログラムが与えられるので，それを復号する問題

```txt
aÁh»öo:¥ì6Ñ×kT:4¡9ÐEÍ
```

```python
from random import seed, randrange

seed(True, version=2)

with open("plaintext.txt", "r") as read, open("ciphertext.txt", "w") as write:
    plaintext = read.read()

    for char in plaintext:
        A = ord(char)
        B = randrange(256)
        ciphertext = chr(A ^ B)
        write.write(ciphertext)

```

## 解説

平文と，ランダムな値で XOR 演算する事で暗号化をしているが， seed 値がわかっているうえ， XOR 演算をしているので， 同じ seed 値の乱数を用いてもう一度 XOR 演算をすることで戻すことができる．

```python
from random import seed, randrange

seed(True, version=2)

with open("ciphertext.txt", "r") as read, open("plaintext.txt", "w") as write:
    ciphertext = read.read()

    for char in ciphertext:
        A = ord(char)
        B = randrange(256)
        plaintext = chr(A ^ B)
        write.write(plaintext)
```

``UACTF{b4d_h4b175_l34d_70_py7h0n2}``
