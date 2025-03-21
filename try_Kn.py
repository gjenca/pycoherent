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
O_nondag=coherent.o_matrix_nodag(orbs)
print('O_nondag matrix:')
print(sympy.pretty(O_nondag))
print('Spectrum nondag:')
print(O_nondag.eigenvals())
O_dag=coherent.o_matrix_dag(orbs)
print('O_dag matrix:')
print(sympy.pretty(O_dag))
print('Spectrum dag:')
print(O_dag.eigenvals())

