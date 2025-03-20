import sympy
import coherent
import perm

n=3
orb1=tuple((i,i) for i in range(1,n+1))
orb2=tuple((i,j) for i in range(1,n+1) for j in range(1,n+1) if i!=j)
orbs=[orb1,orb2]
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

