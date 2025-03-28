import sympy
import coherent
import perm

cycles=perm.cycle_type_to_cyc([2,2,3,3])
p1=perm.cyc_to_perm(cycles)
n=sum(len(c) for c in cycles)
print('permutation:')
for x in range(1,n+1):
    print(x,'->',p1(x))
print('orbits:')
print(perm.orbits([p1],range(1,n+1)))
p2=perm.p_to_p2(p1)
sq=[(x,y) for x in range(1,n+1) for y in range(1,n+1)]
orbs=perm.orbits_single(p2,sq)
print('colors:')
for i,orb in enumerate(orbs):
    print(f'{i}:',orb)
print('inverses:')
print(coherent.inverses(orbs))
print('valencies:')
for i,orb in enumerate(orbs):
    print(f'{i}:',coherent.valency(orb))
O_nondag=coherent.o_matrix_nodag(orbs)
print('O_nondag matrix:')
print(sympy.pretty(O_nondag))
if (O_nondag==O_nondag.T):
    print('Symmetric!')
print('Spectrum nondag:')
print(O_nondag.eigenvals())
O_dag=coherent.o_matrix_dag(orbs)
print('O_dag matrix:')
print(sympy.pretty(O_dag))
print('Spectrum dag:')
print(O_dag.eigenvals())
