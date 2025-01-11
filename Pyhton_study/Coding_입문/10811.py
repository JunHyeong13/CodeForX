# 바구니 뒤집기

n,m = map(int, input().split()) # N, M 두 수가 주어짐.
store = [i for i in range(1, n+1)]
temp = 0 # 역순을 하게 되면, 잠시 저장해둬야 하는 공간이 필요하므로. 
for i in range(m):
    i,j = map(int, input().split())
    temp = store[i-1:j]
    temp.reverse() # 역순을 해주는 구간. 
    print(temp)
    store[i-1:j] = temp

for x in range(n):
    print(store[x], end= " ") # 출력해주는 구간.