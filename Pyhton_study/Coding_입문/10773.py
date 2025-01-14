## 백준 10773번 '제로' ##

K = int(input())
tmp = []
for i in range(K):
    num = input()
    tmp.append(num)
        
for j in range(len(num)): # 길이 값 설정 다시 해야 함. 
    if tmp[j] == 0: # 0이라고 한 수도 지우고, 그 앞에 있는 수도 지워야 함. 
        tmp.pop(tmp[j]) # 앞에 있는 값 지우기. 
        print(tmp)
    elif tmp[j] != 0:
        continue

# 결과 값은, 모두 더한 값을 리턴 해줘야 함. 
result = sum(tmp)
print(result)