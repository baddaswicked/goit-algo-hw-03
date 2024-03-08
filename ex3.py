import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
"""
Пробував зробити через бібліотеку re але через те що в прикладі присутні 
різні типи символів і букв (\\n) прийняв рішення зробити умову перевірки на число,
щоб хардово не прописувати всі варіанти
"""
# def normalize_phone(phones):
#     normal_phone=[]
#     for phone in phones:
#         num="+"
#         next=phone.strip()
#         num+=re.sub(r"[\\nt()\-\s+]","",next)
#         normal_phone.append(num)
#     return normal_phone
# print(normalize_phone(raw_numbers))

def normalize_phone(phones):
    normal_phone=[]

    for phone in phones:
        if phone.startswith("+38"):
            new_num = "+"

            for num in phone:
                if num.isdigit():
                    new_num+=num
                else:
                    continue

        else:
            new_num = "+38"

            for num in phone:
                if num.isdigit():
                    new_num += num
                else:
                    continue

        normal_phone.append(new_num)

    return normal_phone

print("Нормалізовані номери телефонів для SMS-розсилки:", normalize_phone(raw_numbers))