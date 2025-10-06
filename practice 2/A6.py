n=int(input())
s=n%60
M=n//60
m=M%60
h=n//60//60
print('{:02}:{:02}:{:02}'.format(h, m, s))