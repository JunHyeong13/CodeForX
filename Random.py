### 연금복권 720+

# import random

# def generate_random_number():
#     random_number = ' '.join([str(random.randint(1, 46)) for _ in range(7)])
#     return random_number

# # 랜덤 숫자 생성 및 출력
# print(generate_random_number())


### 복권 6/45 
import random

def generate_random_number():
    random_numbers = random.sample(range(1, 46), 6)
    sorted_numbers = sorted(random_numbers)
    random_number = ' '.join(map(str, sorted_numbers))
    return random_number

# 랜덤 숫자 생성 및 출력
print(generate_random_number())