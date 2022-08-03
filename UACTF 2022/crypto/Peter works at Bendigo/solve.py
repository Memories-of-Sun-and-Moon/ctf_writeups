
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