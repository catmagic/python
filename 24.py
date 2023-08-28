import random 
print('Enter your N:')
N=int(input())
a =[random.randint(1, 100) for _ in range(N)]
ap=a[1:N+2:1].copy()
ap.append(a[0])
an=a[0:N-1]
an.insert(0,a[N-1])
print( max(map(sum,zip( map(sum, zip(a,ap),an)))))