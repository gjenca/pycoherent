import sympy
import coherent
import perm

n=4
ps=[]
for k in range(3,n+1):
    p=perm.cyc_to_perm([[1,2,k]],n=n)
    ps.append(perm.p_to_p2(p))
sq=[(x,y) for x in range(1,n+1) for y in range(1,n+1)]
orbs=perm.orbits(ps,sq)
print('colors:')
for i,orb in enumerate(orbs):
    print(f'{i}:',orb)
print('inverses:')
print(coherent.inverses(orbs))
print('valencies:')
for i,orb in enumerate(orbs):
    print(f'{i}:',coherent.valency(orb))
O=coherent.o_matrix_nodag(orbs)
print('O matrix:')
print(sympy.pretty(O))
print('Spectrum:')
print(O.eigenvals())

