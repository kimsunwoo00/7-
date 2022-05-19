import math


a, b ,v = map(int, input().split()) # a 올라가는 높이, b 내려가는 높이, v= 나무길이

day = math.ceil((v-a)/(a-b)) + 1

print(day)
# ceil 함수를 이용하면 소수를 올림 하는 정수를 반환
