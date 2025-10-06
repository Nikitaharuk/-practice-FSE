a=int(input())
a1=int(input())
b=int(input())
b1=int(input())
c=int
d=int
if a%2==0 and a1%2==0: c=1
if a%2==1 and a1%2==1: c=1
if a%2==0 and a1%2==1: c=2
if a%2==1 and a1%2==0: c=2
if b%2==0 and b1%2==0: d=1
if b%2==1 and b1%2==1: d=1
if b%2==0 and b1%2==1: d=2
if b%2==1 and b1%2==0: d=2
if c==d==1:print('yes, black')
if c==d==2:print('yes, white')
if c!=d:print('no')