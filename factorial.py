n=5
c=1
for i in range(n):
    c=c*(i+1)
print(c)
n=5

def fac(n):

    if n==1:
        return 1;
    else:
        return n*fac(n-1)
print(fac(n))