import random 
print('Enter your N:')
N=int(input())
list =[random.randint(0, 1) for _ in range(N)]
print(min(list.count(0),list.count(1)))