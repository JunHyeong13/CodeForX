# 첫 번째 줄에는 각 A,B,C에 대한 값을 넣어 줌.
A, B, C = map(int, input().split())

# def문으로 연산 값을 정리해줌. 
def solution(A,B,C):
    # 첫째 줄에는 (A+B)%C를 출력한다.
    first_result = (A+B)%C 
   
    # 둘째 줄에는 ((A%C)+(B%C))%C를 출력한다. 
    second_result = ((A%C)+(B%C))%C
    
    # 셋째 줄에는 (A×B)%C 를 출력한다.
    third_result = (A*B)%C
    
    # 넷째 줄에는 ((A%C)×(B%C))%C를 출력한다.
    fourth_result = ((A%C)*(B%C))%C
    
    print(first_result, second_result, third_result, fourth_result, sep='\n')

# 마지막 결과 출력. 
solution(A,B,C)