### Map 함수에 대한 설명. 
# map(function, iterable), 첫 번째에는 함수가 오고, 두 번째로는 반복 가능한 자료형(리스트, 튜플)이 오게 됨.
# 아래의 경우, 'int'라는 자료형으로 바꾸어주고, .split()으로 문자에 할당되는 값을 구분시켜 두었음. 
A, B = map(int, input().split())

print(type(A))
print(type(B))

print(A/B)
