"""
첫 번째 컵에 대해 바꿀 컵 정해주기 -> n-1
두 번째 컵에 대해 바꿀 컵 정해주기 -> n-3
... 1까지 반복: (n-1)*(n-3)*...*3*1
"""
N = int(input())
a = 1
for i in range(1,N,2):
    a *= i
    a %= (10**9+7)
print(a)
