import sympy
import coherent
import perm

cycles=[[1,2,3],[4,5],[6,7]]
p1=perm.cyc_to_perm(cycles)
n=sum(len(c) for c in cycles)
print('permutation:')
for x in range(1,n+1):
    print(x,'->',p1(x))
print('orbits:')
print(perm.orbits(p1,range(1,n+1)))
p2=perm.p_to_p2(p1)
sq=[(x,y) for x in range(1,n+1) for y in range(1,n+1)]
orbs=perm.orbits(p2,sq)
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

