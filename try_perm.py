from perm import *

n=6
perms=[]
for k in range(3,n+1):
    p=cyc_to_perm([[1,2,k]],n=n)
    perms.append(p)
print(orbits(perms,list(range(1,n+1))))
