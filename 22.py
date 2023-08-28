import random 
print('Enter your N:')
N=int(input())
a =[random.randint(1, 100) for _ in range(N)]
print('Enter your M:')
M=int(input())
b =[random.randint(1, 100) for _ in range(M)]

print({*a,*b})