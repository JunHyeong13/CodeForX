friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
 
def gift_point(g, i): # i : 특정 친구를 나타내는 인덱스 || g : 친구들 간의 선물을 주고 받은 횟수  
    return sum(g[i]) - sum(list(zip(*g))[i]) #list(zip(*g)) = 행과 열이 뒤바뀐 형태를 얻을 수 있음.  
    # list(zip(*g))[i] : 다른 모든 친구들이 친구 i에게 준 선물의 수를 담고 있는 리스트

def solution(friends, gifts):
    answer = 0
    l = len(friends) # 4
    m = {} # 빈 딕셔너리 선언 (=친구의 이름을 인덱스로 매핑)
    g = [[0] * l for _ in range(l)] # 2차원 리스트 선언. || 초기 값을 0으로 설정한 것. 

    for i, friend in enumerate(friends):
        m[friend] = i # 친구의 이름을 m 변수에 넣는 것. 

    # 각 선물을 준 횟수와 선물을 받은 횟수
    for gift in gifts: 
        a, b = gift.split(" ") # 공백을 기준으로 분류하였기 떄문에, 분류 후 각 a,b에 저장. (선물을 준 사람, 선물을 받은 사람)
        x, y = m[a], m[b] # m[a]에 선물을 준 사람은 x에, m[b]에 선물을 받은 사람은 y에 할당. 
        g[x][y] += 1 

    # 2차원 리스트를 선언
    garr = [0] * l

    # 모든 친구를 순회하며, 선물을 주고받은 횟수를 비교합니다. 선물을 더 많이 준 친구에게 포인트를 부여하고, 받은 선물이 같은 경우 gift_point 함수로 계산하여 포인트를 부여합니다.
    for i in range(l):
        for j in range(i+1, l): # 1부터 l까지 
            a, b = g[i][j], g[j][i]
            if a>b:
                garr[i] += 1
            elif a < b:
                garr[j] += 1
            else:
                i_gp = gift_point(g, i)
                j_gp = gift_point(g, j)
                if i_gp > j_gp:
                    garr[i] += 1 # 선물 지수 값이 높다면
                elif i_gp < j_gp:
                    garr[j] += 1 # 선물 지수 값이 낮다면

    answer = max(garr) # 최댓값을 추출하여 answer 변수에 저장. 
    return answer
