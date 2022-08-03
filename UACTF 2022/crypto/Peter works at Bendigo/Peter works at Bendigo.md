# Peter works at Bendigo

## 問題（ようやく）

一部の桁が欠損したクレジットカードの画像が与えられ，そこからクレジットカード番号を当てる問題

## 解説

<https://www.creditcardvalidator.org/mastercard/bendigo/519244>

クレジットカードの接頭 $4, 5, 6$ 桁は，カードの発行元と発行会社で決まる．

今回の場合は， mastercard の bendigo なので， ``519244`` となる．

残りの $2$ 桁は，最後の桁のチェックサムを利用して，それと合致するもの探すことで，候補を絞ることができる．

```py

card_number = [5,1,9,2,4,4,6,6,8,-1,1,2,5,-1,5,7]
idx_1 = 9
idx_2 = 13

def check_number(ary):
    d_sum = 0
    for i in range(16):
        if i % 2 == 1:
            d_sum += ary[i]
        else:
            num = ary[i] * 2
            if num >= 10:
                d_sum += 1
            d_sum += num % 10

    if d_sum % 10 == 0:
        return True
    else:
        return False

def pr(ary):
    print("UACTF{", end="")
    for i in range(16):
        print(ary[i], end="")
    print("}")

for i in range(10):
    for j in range (10):
        card_number[idx_1] = i
        card_number[idx_2] = j
        if check_number(card_number):
            pr(card_number)
```

```bash
UACTF{5192446680125657}
UACTF{5192446681125557}
UACTF{5192446682125457}
UACTF{5192446683125357}
UACTF{5192446684125257}
UACTF{5192446685125157}
UACTF{5192446686125057}
UACTF{5192446687125957}
UACTF{5192446688125857}
UACTF{5192446689125757}
```

``UACTF{5192446687125957}``

