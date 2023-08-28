from math import sqrt
print('Enter your Sum:')
S = int(input())
print('Enter your Product:')
P = int(input())
# if x and y exist=> exist root (z-x)(z-y)=0 <=>z^2-Sum*z+P=0
if S*S-4*P<0:
	print("error.not correct pair Sum and Produt")
else:
	print((S+sqrt(S*S-4*P))/2,(S-sqrt(S*S-4*P))/2)