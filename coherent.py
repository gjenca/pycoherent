import functools
import sympy
from math import sqrt


@functools.cache
def nabla(a,b,c):

    x,y=c[0]
    count=0
    for x0,z0 in a:
        if x0!=x:
            continue
        for z1,y1 in b:
            if y1==y and z0==z1:
                count=count+1
    return count

def valency(a):

    x,y=a[0]
    count=0
    for x1,y1 in a:
        if x1==x:
            count=count+1
    return count

def inverses(orbs):

    ret={}
    for i,orb1 in enumerate(orbs):
        x,y=orb1[0]
        for j,orb2 in enumerate(orbs):
            if (y,x) in orb2:
                ret[i]=j
                break
    return ret

def o_matrix_nodag(orbs):

    d={}
    nc=len(orbs)
    inv=inverses(orbs)
    val={i:valency(orb) for i,orb in enumerate(orbs)}
    for ai in range(nc):
        for bi in range(nc):
            for ci in range(nc):
                d[(ai,bi,ci)]=sympy.S(nabla(orbs[ai],orbs[bi],orbs[ci]))
    mat_ret=sympy.zeros(nc,nc)
    for ai in range(nc):
        for di in range(nc):
            for bi in range(nc):
                for ci in range(nc):
                    mat_ret[ai,di]+=d[(bi,ci,di)]*(d[(inv[bi],ai,ci)]/val[inv[bi]])
    return mat_ret



if __name__=='__main__':

    cycles=[[1,2],[3]]
    p1=cyc_to_perm(cycles)
    n=sum(len(c) for c in cycles)
    for x in range(1,n+1):
        print(x,'->',p1(x))
    print(orbits(p1,range(1,n+1)))
    p2=p_to_p2(p1)
    sq=[(x,y) for x in range(1,n+1) for y in range(1,n+1)]
    orbs=orbits(p2,sq)
    print('colors:')
    for i,orb in enumerate(orbs):
        print(f'{i}:',orb)
    print('inverses:')
    print(inverses(orbs))
    print('valencies:')
    for i,orb in enumerate(orbs):
        print(f'{i}:',valency(orb))
    #print(r'\nabla_01^2',sc(orbs[0],orbs[1],orbs[2]))
    #print(r'\nabla_10^3',sc(orbs[1],orbs[0],orbs[3]))
    #print(r'\nabla_01^3',sc(orbs[0],orbs[1],orbs[3]))
    O=o_matrix_nodag(orbs)
    print('O matrix:')
    print(sympy.pretty(O))
    print('Spectrum:')
    print(O.eigenvals(multiple=True))
    o1=[]
    o2=[]
    for i in range(1,5):
        for j in range(1,5):
            if i==j:
                o1.append((i,j))
            else:
                o2.append((i,j))
    K=[tuple(o1),tuple(o2)]
    O=o_matrix_nodag(K)
    print('O matrix:')
    print(sympy.pretty(O))
    print('Spectrum:')
    print(O.eigenvals(multiple=True))

