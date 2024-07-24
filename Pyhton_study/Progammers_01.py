friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
 
 
'''

[문제 설명]
선물을 직접 전하기 힘들 때 카카오톡 선물하기 기능을 이용해 축하 선물을 보낼 수 있습니다. 당신의 친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하려고 합니다.

두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
예를 들어 A가 B에게 선물을 5번 줬고, B가 A에게 선물을 3번 줬다면 다음 달엔 A가 B에게 선물을 하나 받습니다.
두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.
예를 들어 A가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 A의 선물 지수는 -7입니다. B가 친구들에게 준 선물이 3개고 받은 선물이 2개라면 B의 선물 지수는 1입니다. 만약 A와 B가 선물을 주고받은 적이 없거나 정확히 같은 수로 선물을 주고받았다면, 다음 달엔 B가 A에게 선물을 하나 받습니다.
만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.
위에서 설명한 규칙대로 다음 달에 선물을 주고받을 때, 당신은 선물을 가장 많이 받을 친구가 받을 선물의 수를 알고 싶습니다.

친구들의 이름을 담은 1차원 문자열 배열 friends 이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 gifts가 매개변수로 주어집니다. 이때, 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return 하도록 solution 함수를 완성해 주세요.

''' 
 
 
 
 
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