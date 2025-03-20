
def cyc_to_perm(cyc,n=None):

    d={}
    d_inv={}
    if n:
        for k in range(1,n+1):
            d[k]=k
            d_inv[k]=k
    for c in cyc:
        for x,y in zip(c,c[1:]+[c[0]]):
            d[x]=y
            d_inv[y]=x

    def ret_f(x,inverse=False):
        nonlocal d,d_inv
        if inverse:
            return d_inv[x]
        else:
            return d[x]

    return ret_f

class FoundY(Exception):

    def __init__(self,y):

        self.y=y

def orbits_single(p,xs):

    ret=[]
    unseen=set(xs)
    while unseen:
        x=unseen.pop()
        orb=[]
        while True:
            orb.append(x)
            x=p(x)
            if x not in unseen:
                break
            unseen.remove(x)
        ret.append(tuple(orb))
    return ret

def orbits(perms,xs):

    ret=[]
    unseen=set(xs)
    while unseen:
        x=unseen.pop()
        orb=set()
        orb.add(x)
        while True:
            try:
                for x in orb:
                    for p in perms:
                        for y in (p(x),p(x,inverse=True)):
                            if y in unseen:
                                raise FoundY(y)
            except FoundY as fy:
                orb.add(fy.y)
                unseen.remove(fy.y)
            else:
                break
        ret.append(tuple(orb))
    return ret

def p_to_p2(p):

    def ret_f(pair,inverse=False):
        return (p(pair[0],inverse=inverse),p(pair[1],inverse=inverse))

    return ret_f

