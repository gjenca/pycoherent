import sympy
import coherent
import perm

n=3
orbs=[((i,j),) for i in range(1,n+1) for j in range(1,n+1)]

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
