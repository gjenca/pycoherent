
def cyc_to_perm(cyc):

    d={}
    for c in cyc:
        for x,y in zip(c,c[1:]+[c[0]]):
            d[x]=y

    def ret_f(x):

        return d[x]

    return ret_f

def orbits(p,xs):

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

def p_to_p2(p):

    def ret_f(pair):
        return (p(pair[0]),p(pair[1]))

    return ret_f

