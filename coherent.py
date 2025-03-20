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
                #d[(ai,bi,ci)]=nabla(orbs[ai],orbs[bi],orbs[ci])
    mat_ret=sympy.zeros(nc,nc)
    for ai in range(nc):
        for di in range(nc):
            for bi in range(nc):
                for ci in range(nc):
                    mat_ret[ai,di]+=d[(bi,ci,di)]*(d[(inv[bi],ai,ci)]/val[inv[bi]])
                    #mat_ret[ai,di]+=d[(bi,ci,di)]*(d[(ai,inv[ci],bi)]/val[ci])
    return mat_ret



