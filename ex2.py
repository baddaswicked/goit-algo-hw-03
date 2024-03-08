import random

def get_numbers_ticket(min:int, max:int, quantity:int):
    lst=[]
    for x in range(1000):
        random_num=random.randint(min,max)
        if random_num in lst:
            continue
        else:
            lst.append(random_num)
    return lst[:quantity]
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

