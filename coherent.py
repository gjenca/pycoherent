import functools
import sympy
from math import sqrt
import itertools

def symmetrize(color):

    ret=set(color)
    for x,y in color:
        ret.add((y,x))
    return tuple(sorted(ret))

def remainder(colors,n):

    ret=set((i,j) for i in range(1,n+1) for j in range(1,n+1))
    for color in colors:
        ret=ret-set(color)
    return tuple(sorted(ret))

def from_colorfun(it,colorfun):

    values=list(it)
    colors=[]
    ret_d={}
    for x,y in itertools.product(values,values):
        color=colorfun(x,y)
        if color not in colors:
            colors.append(color)
            ret_d[colors.index(color)]=[]
        ret_d[colors.index(color)].append((x,y))
    ret=sorted(tuple(sorted(value)) for value in ret_d.values())
    return ret


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

def inverses(colors):

    ret={}
    for i,color1 in enumerate(colors):
        x,y=color1[0]
        for j,color2 in enumerate(colors):
            if (y,x) in color2:
                ret[i]=j
                break
    return ret

def o_matrix_nodag(colors):

    d={}
    nc=len(colors)
    inv=inverses(colors)
    val={i:sympy.sympify(valency(color)) for i,color in enumerate(colors)}
    for ai in range(nc):
        for bi in range(nc):
            for ci in range(nc):
                d[(ai,bi,ci)]=sympy.sympify(nabla(colors[ai],colors[bi],colors[ci]))
                #d[(ai,bi,ci)]=nabla(colors[ai],colors[bi],colors[ci])
    mat_ret=sympy.zeros(nc,nc)
    for ai in range(nc):
        for di in range(nc):
            for bi in range(nc):
                for ci in range(nc):
                    mat_ret[ai,di]+=d[(bi,ci,di)]*(d[(inv[bi],ai,ci)]/val[inv[bi]])
                    #mat_ret[ai,di]+=d[(bi,ci,di)]*(d[(ai,inv[ci],bi)]/val[ci])
    return mat_ret

def o_matrix_dag(colors):

    d={}
    nc=len(colors)
    inv=inverses(colors)
    val={i:sympy.sympify(valency(color)) for i,color in enumerate(colors)}
    for ai in range(nc):
        for bi in range(nc):
            for ci in range(nc):
                d[(ai,bi,ci)]=sympy.sympify(nabla(colors[ai],colors[bi],colors[ci]))
                #d[(ai,bi,ci)]=nabla(colors[ai],colors[bi],colors[ci])
    mat_ret=sympy.zeros(nc,nc)
    for ai in range(nc):
        for di in range(nc):
            for bi in range(nc):
                for ci in range(nc):
                    mat_ret[ai,di]+=\
                            sympy.sqrt((val[ai]*val[di]))/(val[bi]*val[ci])*\
                            nabla(colors[bi],colors[ci],colors[ai])*nabla(colors[bi],colors[ci],colors[di])
    return mat_ret



