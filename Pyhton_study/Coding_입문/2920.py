# 음계 
# c = 1, d = 2, e = 3, f = 4, g = 5, a = 6, b = 7, C = 8
# 값을 입력받음 

tmp = []
n = input().split()

if n == ['1', '2', '3', '4', '5', '6', '7', '8']:
    print("ascending")
elif n == ['8', '7', '6', '5', '4', '3', '2', '1']:
    print("descending")
else:
    print("mixed")